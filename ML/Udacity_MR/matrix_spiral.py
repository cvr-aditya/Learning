


mat = [
  [1, 2, 3],
  [4, 5, 6]
]
r = 5
c = 4


def print_spiral(r, c):

    curr_row = 0
    curr_col = 0

    while curr_row < r and curr_col < c:

        for i in range(curr_col, c):
            print mat[curr_row][i],
        curr_row += 1

        for i in range(curr_row, r):
            print mat[i][c-1],

        c -= 1

        if curr_row < r:
            for i in range(c-1, curr_col-1, -1):
                print mat[r-1][i],
            r -= 1

        if curr_col < c:
            for i in range(r-1, curr_row-1, -1):
                print mat[i][curr_col],
            curr_col += 1

print_spiral(len(mat), len(mat[0]))
# print len(mat[0])


res = []
for i in range(3):
    res.append([0]*3)
print res