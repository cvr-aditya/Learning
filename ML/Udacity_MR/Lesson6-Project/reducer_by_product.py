#!/usr/bin/env python

import sys


def reducer():
    total_cost = 0
    prev_product = None
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        curr_product, cost = data

        if prev_product and prev_product != curr_product:
            print "{0}\t{1}".format(prev_product, total_cost)
            total_cost = 0

        prev_product = curr_product
        total_cost += float(cost)

    if prev_product is not None:
        print "{0}\t{1}".format(prev_product, total_cost)


if __name__ == "__main__":
    reducer()