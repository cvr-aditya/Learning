#!/usr/bin/env python

import sys


def reducer():
    sales = 0
    total_sales = 0
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        curr_product, cost = data
        sales += 1
        total_sales += float(cost)

    print "{0}\t{1}".format(sales, total_sales)

reducer()