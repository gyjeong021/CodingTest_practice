import sys

n_list = []

for i in range(9) :
    n = int(sys.stdin.readline())
    n_list.append(n)

print(max(n_list))
print((n_list.index(max(n_list))+1))