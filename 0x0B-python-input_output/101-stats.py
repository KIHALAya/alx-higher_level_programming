#!/usr/bin/python3
"""Reads from standard input and computes metrics."""


def print_statistics(size, stats):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        stats (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for each in sorted(stats_codes):
        print("{}: {}".format(key, stats[each]))


if __name__ == "__main__":
    import sys

    size = 0
    stats = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, stats)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if stats.get(line[-2], -1) == -1:
                        stats[line[-2]] = 1
                    else:
                        stats[line[-2]] += 1
            except IndexError:
                pass

        print_statistics(size, stats)

    except KeyboardInterrupt:
        print_statistics(size, stats)
        raise
