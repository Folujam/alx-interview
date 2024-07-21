#!/usr/bin/python3
"""Log parsing Module"""
import sys
#  this docd out script, was initial idea. dosent work yet
"""import re


#  script reads from stdin line by line
total_size = 0
status_counts = 0
"""
#  for line in sys.stdin:
#   pattern = r"^(?P<ip>\S+) - \[(?P<date>.+)\] \
#        'GET /projects/260 HTTP/1.1' (?P<status>\d{3}) (?P<size>\d+)$"
"""    match = re.match(pattern, line)

    if match:
        ip = match.group('ip')
        date = match.group('date')
        status = match.group('status')
        size = match.group('size')

    total_size += int(size)
    status_counts[status] = status_counts.get(status, 0) + 1

    try:
        for i, line in enumerate(sys.stdin, 1):
            # process line
            if i % 10 == 0:
                print('Total file size:', total_size)
                for status, count in sorted(status_counts.items()):
                    print(status, ':', count)
    except KeyboardInterrupt:
        print('Interrupted')

#  if line != format skip
#  after 10lines/signal(ctrl+C) print
#  total file size = all read file sizes sumed
#  implement status code (must be integer) -
#  <sc>: <num> (printed ascd order)
"""


def print_msg(dict_sc, total_file_size):
    """prints dict message"""
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in dict_sc.keys()):
                    dict_sc[code] += 1

            if (counter == 10):
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)
