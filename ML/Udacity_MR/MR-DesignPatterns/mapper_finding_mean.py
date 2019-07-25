#!/usr/bin/env python

import sys
from datetime import datetime


def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 6:
            continue

        date = data[0]
        cost = data[4]
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)

if __name__ == "__main__":
    mapper()
