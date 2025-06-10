import sys

n, m = map(int, sys.stdin.readline().split())
n_basket = n * [0]

for i in range(m) :
    one, two, num = map(int, sys.stdin.readline().split())
    for j in range(one, two+1) :
        n_basket[j-1] = num

for i in n_basket :
    print(i, end=" ")