import sys

n, m = map(int, sys.stdin.readline().split())
n_box = [i for i in range(1,n+1)]

for i in range(m) :
    i_box, j_box = map(int, sys.stdin.readline().split())
    x = n_box[i_box-1]
    n_box[i_box-1] = n_box[j_box-1]
    n_box[j_box-1] = x

for i in n_box :
    print(i, end=" ")