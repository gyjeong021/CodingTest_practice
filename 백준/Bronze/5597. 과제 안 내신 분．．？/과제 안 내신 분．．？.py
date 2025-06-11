import sys

list = []
s_list = []

for i in range(28) :
    num = int(sys.stdin.readline())
    list.append(num)

for i in range(1,31) :
    if i not in list :
        s_list.append(i)

print(min(s_list))
print(max(s_list))