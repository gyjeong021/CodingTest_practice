one = int(input())
two = int(input())

print(one*(two%10))
print(one*((two//10)%10))
print(one*(two//100))
print(one*two)