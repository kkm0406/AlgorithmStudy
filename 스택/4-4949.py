import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence[0] == '.':
        break
    flag = True
    stack = []
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if flag and not stack:
        print('yes')
    else:
        print('no')
