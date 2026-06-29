# api_aggregator.py
import requests
import json
import os
from datetime import datetime
from functools import wraps
import time
from dotenv import load_dotenv

load_dotenv()

# ── Decorators ──────────────────────────────────────────────
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  [{func.__name__}] completed in {elapsed:.2f}s")
        return result
    return wrapper

def retry(max_attempts=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    last_exception = e
                    print(f"  Attempt {attempt+1}/{max_attempts} failed: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            if last_exception:
                raise last_exception
            raise RuntimeError("Retry decorator failed without capturing an exception.")
        return wrapper
    return decorator

# ── API Calls ────────────────────────────────────────────────
@timer
@retry(max_attempts=3)
def get_weather(city_name):
    if not city_name or not city_name.strip():
        raise ValueError("City name cannot be empty.")

    city_lat, city_lon = get_latlong(city_name)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": city_lat,
        "longitude": city_lon,
        "current_weather": True
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()["current_weather"]
    return {
        "city": city_name,
        "temperature_c": data["temperature"],
        "wind_speed_kmh": data["windspeed"],
        "fetched_at": datetime.now().isoformat()
    }

@timer
@retry(max_attempts=3)
def get_latlong(city_name):
    print(f"Fetching latitude & longitude for {city_name}...")
    url_latlon = "https://geocoding-api.open-meteo.com/v1/search"
    params_latlon = {
        "name": city_name,
        "country": "IN",
        "count": 1
    }

    response_latlon = requests.get(url_latlon, params=params_latlon, timeout=10)
    response_latlon.raise_for_status()
    data = response_latlon.json().get("results", [])

    if not data:
        raise ValueError("City not found.")

    city_lat = float(data[0]["latitude"])
    city_lon = float(data[0]["longitude"])
    print(f"Fetching weather for {city_name} (lat: {city_lat}, lon: {city_lon})...")
    return city_lat, city_lon

@timer
@retry(max_attempts=3)
def get_top_repos(search_term, count=5):
    url = "https://api.github.com/search/repositories"
    params = {"q": search_term, "sort": "stars", "per_page": count}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    repos = response.json()["items"]
    # Generator expression — memory efficient
    return [
        {"name": r["full_name"], "stars": r["stargazers_count"], "url": r["html_url"]}
        for r in repos
    ]

@timer
@retry(max_attempts=3)
def get_programming_joke():
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    joke = response.json()[0]
    return {"setup": joke["setup"], "punchline": joke["punchline"]}

# ── Context manager for saving results ──────────────────────
from contextlib import contextmanager

@contextmanager
def results_file(filename):
    print(f"\nOpening {filename} for writing...")
    f = open(filename, "w", encoding="utf-8")
    try:
        yield f
    finally:
        f.close()
        print(f"Saved results to {filename}")

# ── Main ─────────────────────────────────────────────────────
def main():
    print("Fetching data from multiple APIs...\n")

    results = {
        "generated_at": datetime.now().isoformat(),
        "weather": get_weather("pune"),
        "top_repos": get_top_repos("generative AI"),
        "joke": get_programming_joke()
    }

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results_{timestamp}.json"

    with results_file(filename) as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Pretty print summary
    print("\n── Summary ──────────────────────")
    print(f"Weather in {results['weather']['city']}: "
          f"{results['weather']['temperature_c']}°C & {results['weather']['wind_speed_kmh']} kmph")
    print(f"\nTop Gen AI repos:")
    for repo in results["top_repos"]:
        print(f"  ⭐ {repo['stars']:,}  {repo['name']}")
    print(f"\nJoke: {results['joke']['setup']}")
    print(f"  → {results['joke']['punchline']}")

if __name__ == "__main__":
    main()