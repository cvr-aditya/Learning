#!/usr/bin/env python

import sys


def reducer():
    prev_day = None
    cost = 0
    for line in sys.stdin:

        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        day, curr_cost = data
        if prev_day and prev_day != day:
            print "{0}\t{1}".format(prev_day, cost)
            cost = 0

        prev_day = day
        cost += float(curr_cost)

    if prev_day is not None:
        print "{0}\t{1}".format(prev_day, cost)

reducer()
