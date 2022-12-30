import sys

S = sys.stdin.readline().strip()
flag = False
result = ""
tmp = ""
for i in S:
    if not flag:
        if i == '<':
            flag = True
            tmp += i
        elif i == ' ':
            tmp += i
            result += tmp
            tmp = ""
        else:
            tmp = i + tmp
    else:
        tmp += i
        if i == '>':
            flag = False
            result += tmp
            tmp = ""

print(result + tmp)
