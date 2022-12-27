import sys

word = sys.stdin.readline().strip()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha:
    if i in word:
        word = word.replace(i, ",")

cnt = word.count(',')
word = word.replace(",", "")
print(cnt+len(word))

