#!/usr/bin/python3
'''
Usage:
    ./0-generator | ./0-stats.py
'''

if __name__ == '__main__':
    import sys

    status_counter = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0,
            }

    log_entry_count = 1
    file_size = 0

    def parse_line(log_entry)-> int :
        """
        Read, prase, and extract relevant data from a given log entry.
        Args:
            log_entry (str): A log entry to be parsed

        Returns:
            int: The siez of the file indicated in the log entry.
        """
        try:
            parsed_entry = log_entry.split()
            status_code = parsed_entry[-2]
            if status_code in status_counter.keys():
                status_counter[status_code] += 1
            return int(parsed_entry[-1])
        except Exception:
            return 0

    def print_stats()-> str:
        print(f"File size: {file_size}")
        for key in sorted(status_counter.keys()):
            if status_counter[key]:
                print(f"{key}: {status_counter[key]}")

    try:
        for log_entry in sys.stdin:
            file_size += parse_line(log_entry)
            if log_entry_count % 10 == 0:
                print_stats()
            log_entry_count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
