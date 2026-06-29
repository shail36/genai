logs = [
    "ERROR | 2026-06-09 09:45 | Disk full | Retry failed",
    "WARNING | 2026-06-09 09:50 | High memory usage | Threshold exceeded",
    "INFO | 2026-06-09 10:00 | Job completed | Success",
    "ERROR | 2026-06-09 10:15 | Network timeout | Connection lost"
]
# Log -> Split -> append (in dict) -> Counter -> filter (for errors)

def parse_logs(log_lines):
    parsed = []
    for line in log_lines:
        level, timestamp, message, detail = line.split(" | ")
        parsed.append({
            "level": level,
            "timestamp": timestamp,
            "message": message,
            "detail": detail
        })
    return parsed

parsed_logs = parse_logs(logs)
print("Parsed Logs:")
print(parsed_logs)

from collections import Counter

levels = [log["level"] for log in parsed_logs]
count = Counter(levels)
print("Log level counts:")
print(count)

errors = [log for log in parsed_logs if log["level"] == "ERROR"]
print("Errors found:")
print(errors)

