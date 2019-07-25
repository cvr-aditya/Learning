#!/usr/bin/env python

import sys


def reducer():
    total_cost = 0
    global_max = 0
    site = None
    prev_site = None
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        curr_site, hits = data
        hits = int(hits)
        if prev_site and prev_site != curr_site:
            if total_cost > global_max:
                global_max = total_cost
                site = prev_site
            total_cost = 0

        prev_site = curr_site
        total_cost += hits

    if total_cost > global_max:
        global_max = total_cost
        site = prev_site
    print "{0}\t{1}".format(site, global_max)


if __name__ == "__main__":
    reducer()