#!/usr/bin/python3

"""Stats"""


def print_stats(file_size, status_codes):
    """Print stats"""
    print("File size: {:d}".format(file_size))
    for k, v in sorted(status_codes.items()):
        print("{:s}: {:d}".format(k, v))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            tokens = line.split()
            file_size += int(tokens[-1])
            if tokens[-2] in status_codes:
                status_codes[tokens[-2]] += 1
            if count == 10:
                print_stats(file_size, status_codes)
                count = 0
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
    print_stats(file_size, status_codes)
