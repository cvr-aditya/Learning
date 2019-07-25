# !/bin/python


# Complete the minimumBribes function below.
def minimumBribes(q):
    res = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print "Too chaotic"
            return

    for i in range(len(q)):
        for j in range(i, len(q)):
            if q[i] > q[j]:
                q[i], q[j] = q[j], q[i]
                res += 1
    print res


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
