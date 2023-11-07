#!/usr/bin/python3
"""
101-stats - Script that reads stdin line by line and computes metrics.
"""
import sys
from collections import defaultdict


def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)
            except (ValueError, IndexError):
                pass

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
