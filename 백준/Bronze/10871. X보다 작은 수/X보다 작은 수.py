import sys

N, X = map(int, sys.stdin.readline().split())

A_list = list(map(int, sys.stdin.readline().split()))

for i in A_list :
    if i < X :
        print(i, end = " ")
