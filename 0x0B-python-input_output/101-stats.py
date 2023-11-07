#!/usr/bin/python3
"""Reads from standard input and computes metrics."""


def _stats(size, stats):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(stats):
        print("{}: {}".format(key, stats[key]))


if __name__ == "__main__":
    import sys

    size = 0
    stats = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                _stats(size, stats)
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

        _stats(size, stats)

    except KeyboardInterrupt:
        _stats(size, stats)
        raise
