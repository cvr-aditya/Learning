#!/usr/bin/env python

import sys
from collections import defaultdict

def reducer():

    words_dict = defaultdict(list)
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        word, node = data
        words_dict[word].append(int(node))

    for word in words_dict:
        print "{0}\t{1}\t{2}".format(word, len(words_dict[word]), words_dict[word])

reducer()