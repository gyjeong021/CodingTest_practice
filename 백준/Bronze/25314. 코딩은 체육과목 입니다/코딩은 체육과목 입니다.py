N = int(input())
answer = ""

while N // 4 > 0 :
    answer += "long "
    N -= 4

answer += "int"

print(answer)