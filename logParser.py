import sys
import re
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)'
    match = re.match(pattern, line)
    if match:
        return {'datetime': match.group(1), 'level': match.group(2), 'message': match.group(3)}
    return {}


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)


def display_log_counts(counts: dict):
    print("Log level counts:")
    for level, count in counts.items():
        print(f"{level}: {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <log_file_path> [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    if len(logs) == 0:
        return

    all_counts = count_logs_by_level(logs)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        logs = filter_logs_by_level(logs, level)
        display_log_counts(all_counts)
        for log in logs:
            print(f"{log['datetime']} {log['level']} {log['message']}")
    else:
        display_log_counts(all_counts)


if __name__ == "__main__":
    main()
