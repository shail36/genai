# # # ##def number(n):
# # # ##    for i in range(1,n+1):
# # # ##        num = yield i

# # # ##print(list(number(10)))

# # # ##for num in number(10):
# # # ##    print(num)

# # # file_location = r"C:\Users\sagar\GEN_AI\week01\sample.txt"
# # # def read_file(file):
# # #     try:
# # #         with open(file,'r') as file:
# # #             for line in file:
# # #                  yield line.strip()
# # #     except FileNotFoundError:
# # #         print(f"Error: The file '{file}' was not found.")
# # #         return None
    

# # # for line in read_file(file_location):
# # #     if line is not None:
# # #         print(line)

# # import requests

# # # Simple GET request
# # # response = requests.get("https://api.github.com/users/torvalds")
# # # print(response.status_code)   # 200
# # # print(response.json())        # dict with user data

# # # # GET with query parameters
# # # params = {"q": "python", "sort": "stars", "per_page": 5}
# # # response = requests.get(
# # #     "https://api.github.com/search/repositories",
# # #     params=params
# # # )
# # # data = response.json()
# # # print(data)
# # # for repo in data["items"]:
# # #     print(repo["full_name"], "⭐", repo["stargazers_count"]


# from datetime import datetime

# import requests
# import os
# from dotenv import load_dotenv

# # load_dotenv()

# # headers = {
# #     "Content-Type": "application/json",
# #     "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
# # }

# # body = {
# #     "model": "gpt-4o-mini",
# #     "messages": [
# #         {"role": "system", "content": "You are a helpful assistant."},
# #         {"role": "user",   "content": "What is RAG in Gen AI?"}
# #     ],
# #     "temperature": 0.7,
# #     "max_tokens": 200
# # }

# # response = requests.post(
# #     "https://api.openai.com/v1/chat/completions",
# #     headers=headers,
# #     json=body
# # )

# # if response.status_code == 200:
# #     reply = response.json()["choices"][0]["message"]["content"]
# #     print(reply)
# # else:
# #     print(f"Error {response.status_code}: {response.json()}")

# def get_weather(city_name):
#     url = "https://api.open-meteo.com/v1/forecast"
#     params = {
#         "latitude": 26
#         "longitude": 13.41,
#         "current_weather": True
#     }
#     response = requests.get(url, params=params, timeout=10)
#     response.raise_for_status()
#     data = response.json()["current_weather"]
#     return {
#         "city": city_name,
#         "temperature_c": data["temperature"],
#         "wind_speed_kmh": data["windspeed"],
#         "fetched_at": datetime.now().isoformat()
#     }

# results = get_weather("kanpur")
# print(results)

import requests

def get_coordinates(city, country="India"):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "city": city,
        "country": country,
        "format": "json"
    }
    headers = {
        "User-Agent": "GEN_AI_Project/1.0 (shashank@example.com)"  
        # Replace with your email or project name
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            print(f"{city} → Latitude: {lat}, Longitude: {lon}")
        else:
            print("No results found.")
    else:
        print(f"Error {response.status_code}: {response.text}")

# Example usage
get_coordinates("Mulshi")
get_coordinates("Mumbai")


