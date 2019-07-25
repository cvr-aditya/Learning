#!/usr/bin/env python
import sys
import csv
import re


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
        data = line[4]
        node = line[0]
        all_words = [word.lower() for word in re.findall(r"[a-zA-Z]+", data)]
        for word in all_words:
            print "{0}\t{1}".format(word, node)

if __name__ == "__main__":
    mapper()