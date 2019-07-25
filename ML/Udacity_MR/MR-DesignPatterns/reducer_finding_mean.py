#!/usr/bin/env python

import sys
from collections import defaultdict


def reducer():
    day_cost = defaultdict(list)
    for line in sys.stdin:

        data = line.strip().split("\t")

        if len(data) != 2:
            continue
        weekday, cost = data
        day_cost[weekday].append(float(cost))

    for day in day_cost:
        mean_price = (sum(day_cost[day])*1.0) / len(day_cost[day])
        print "{0}\t{1}".format(day, mean_price)

reducer()