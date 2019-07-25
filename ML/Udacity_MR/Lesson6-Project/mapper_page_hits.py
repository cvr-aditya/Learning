#!/usr/bin/env python

import sys


def mapper():

    for line in sys.stdin:
        data = line.strip().split(" ")
        if len(data) != 10:
            continue
        page_name = data[6]
        print "{0}\t{1}".format(page_name, 1)

mapper()
