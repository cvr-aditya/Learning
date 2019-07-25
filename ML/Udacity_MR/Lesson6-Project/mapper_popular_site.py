#!/usr/bin/env python

import sys


def mapper():

    for line in sys.stdin:
        data = line.strip().split(" ")
        if len(data) != 10:
            continue
        remove_string = "http://www.the-associates.co.uk"
        page_name = data[6]
        if page_name.startswith(remove_string):
            page_name = page_name.split(remove_string)[1]
        print "{0}\t{1}".format(page_name, 1)

mapper()
