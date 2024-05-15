#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""

import sys
import signal


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


def print_stats():
    global total_size
    global status_codes

    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

total_size = 0
status_codes = {}

signal.signal(signal.SIGINT, signal_handler)

try:
    for line_num, line in enumerate(sys.stdin, start=1):
        try:
            ip, _, _, status, size = line.split()[0], line.split()[8], line.split()[10], line.split()[7], line.split()[9]
            size = int(size)
            if status.isdigit():
                status = int(status)
                if status in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_codes[status] = status_codes.get(status, 0) + 1
            total_size += size
        except Exception as e:
            continue

        if line_num % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
