#!/usr/bin/python3
"""
This module parses a log, which it receives
from the standard input of the I/O stream
"""

import sys
import re
import signal


ip_p = r'\d+.\d+.\d+.\d+'
sp_dash_p = r' - '
date_p = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]'
sp = r' '
query_verb_p = r'"[A-Z]+ /[a-z]+/\d+ HTTP/\d.\d"'
st_p = r'\d{3}'
fs_p = r'\d+'
_ptn = ip_p + sp_dash_p + date_p + sp + query_verb_p + sp + st_p + sp + fs_p
stat = {}
line_counter = 0
file_size = 0


def display_statistics(file_size, stat):
    """
    displays the statistics data to the screen (standard output)

    Args:
        file_size - the number of file sizes, accumulated so far
        stat - a dictionary that storesr the statistucs data
    """
    print("File size: {0}".format(file_size))
    for k in sorted(stat.keys()):
        if isinstance(stat.get(k), int):
            print("{}: {}".format(k, stat.get(k)))


def interrupt_handler(signum, frame):
    """
    triggers when the interupt signal event occurs and exits with 0

    Args:
        signum - the signal number
        frame - the frame
    """
    display_statistics(file_size, stat)
    sys.exit(0)


signal.signal(signal.SIGINT, interrupt_handler)

for line in sys.stdin:
    if line_counter % 10 == 0 and line_counter > 0:
        display_statistics(file_size, stat)

    match = re.search(_ptn, line)
    if (len(match.group()) < 50):
        continue
    data = match.group().split(' ')
    status_code = data[-2]
    f_size = data[-1]

    if not stat.get(status_code):
        stat[status_code] = 1
    else:
        stat[status_code] += 1
    file_size += int(f_size)
    line_counter += 1
