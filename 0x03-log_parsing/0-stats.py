#!/usr/bin/python3
"""
This module parses a log, which it receives
from the standard input of the I/O stream
"""

import sys
import re
import signal
import time
from functools import wraps


p1 =  r'\d+.\d+.\d+.\d+ - '
p2 = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
p3 = r'"[A-Z]+ /[a-z]+/\d+ HTTP/\d.\d" \d{3} \d+'
_ptn = p1 + p2 + p3
stat = {}
line_counter = 0
file_size = 0
track_d = 0


def is_valid(status_code: str) -> bool:
    """validates a given status code

    Args:
        status_code - the status code to be validated

    Returns:
        True is returned if the passsed status
        code is valid else False is returned
    """
    _st = ['200', '301', '400', '401', '403', '404', '405', '500']
    if status_code in _st:
        return True
    return False


def track_display(fn):
    """tracks the number of times when a function is called"""
    global track_d

    @wraps(fn)
    def wrapper():
        """updates the number of of times a function is called

        Args:
            fn- the function to be tracked
        """
        global track_d
        track_d += 1
        return fn()
    return wrapper


@track_display
def display_statistics():
    """
    displays the statistics data to the screen (standard output)

    Args:
        file_size - the number of file sizes, accumulated so far
        stat - a dictionary that storesr the statistucs data
    """
    print("File size: {0}".format(file_size))
    for k in sorted(stat.keys()):
        if isinstance(stat.get(k), int) and is_valid(k):
            print("{}: {}".format(k, stat.get(k)))


def interrupt_handler(signum, frame):
    """
    triggers when the interupt signal event occurs and exits with 0

    Args:
        signum - the signal number
        frame - the frame
    """
    display_statistics()
    time.sleep(0.1)
    sys.exit(0)



signal.signal(signal.SIGINT, interrupt_handler)

for line in sys.stdin:
    if line_counter % 10 == 0 and line_counter > 0:
        display_statistics()

    matched = re.search(_ptn, line)
    try:
        matched = matched.group()
    except AttributeError:
        matched = None
    if (not matched):
        line_counter += 1
        continue
    data = matched.split(' ')
    status_code = data[-2]
    f_size = data[-1]
    try:
        f_size = int(f_size)
    except ValueError:
        f_size = 0

    if not stat.get(status_code):
        stat[status_code] = 1
    else:
        stat[status_code] += 1
    file_size += f_size
    line_counter += 1

if track_d == 0:
    display_statistics()
else:
    display_statistics()
