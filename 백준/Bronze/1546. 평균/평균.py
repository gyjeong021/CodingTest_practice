import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
max = max(score)
sum = 0

for i in range(n) :
    sum += score[i] / max * 100

print(sum/n)
