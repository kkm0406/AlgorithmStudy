import sys

s = sys.stdin.readline().rstrip()

for i in s:
    if 65 <= ord(i) <= 90:
        num = ord(i) + 13
        if num > 90:
            print(chr(65 + num - 90-1), end="")
        else:
            print(chr(num), end="")
    elif 97 <= ord(i) <= 122:
        num = ord(i) + 13
        if num > 122:
            print(chr(97 + num - 122 - 1), end="")
        else:
            print(chr(num), end="")
    else:
        print(i, end="")
