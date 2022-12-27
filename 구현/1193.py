import sys

n = int(sys.stdin.readline())

line = 0
maxNum = 0
while n > maxNum:
    line += 1
    maxNum += line

a = 0
b = 0
if line % 2 == 0:
    a = line - (maxNum - n)
    b = maxNum - n + 1
else:
    a = maxNum - n + 1
    b = line - (maxNum - n)

print(f"{a}/{b}")
