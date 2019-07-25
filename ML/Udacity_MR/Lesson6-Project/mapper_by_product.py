#!/usr/bin/python
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 6:
            continue
        product, cost = data[3], data[4]
        print "{0}\t{1}".format(product, cost)

if __name__ == "__main__":
    mapper()