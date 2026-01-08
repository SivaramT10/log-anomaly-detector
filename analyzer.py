import statistics
from collections import defaultdict

def parse_logs(file_path):
    """
    Very simple parser: counts log entries per time window.
    Here we simulate time windows by line number buckets.
    """
    buckets = defaultdict(int)
    with open(file_path, "r") as f:
        for i, _ in enumerate(f):
            bucket = i // 5   # 5 log lines per time window
            buckets[bucket] += 1
    return list(buckets.values())

def detect_anomalies(counts, threshold=2):
    if len(counts) < 2:
        return []

    mean = statistics.mean(counts)
    std = statistics.stdev(counts)

    anomalies = []
    for idx, count in enumerate(counts):
        if count > mean + threshold * std:
            anomalies.append((idx, count))
    return anomalies

if __name__ == "__main__":
    log_counts = parse_logs("sample_logs.log")
    anomalies = detect_anomalies(log_counts)

    print("Log activity per window:", log_counts)
    if anomalies:
        print("\nDetected anomalies:")
        for window, value in anomalies:
            print(f"Window {window}: {value} log events")
    else:
        print("\nNo anomalies detected.")
