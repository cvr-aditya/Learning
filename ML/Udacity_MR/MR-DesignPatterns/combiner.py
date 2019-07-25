#!/usr/bin/env python

import sys
from collections import defaultdict


def combiner():
    day_cost = defaultdict(list)
    for line in sys.stdin:

        data = line.strip().split("\t")

        if len(data) != 2:
            continue
        weekday, cost = data
        day_cost[weekday].append(float(cost))

    for day in day_cost:
        print "{0}\t{1}".format(day, sum(day_cost[day]))

combiner()