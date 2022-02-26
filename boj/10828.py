import sys
sys.stdin = open('10828.txt')
input = sys.stdin.readline
n = int(input())


stack = []
answer = []

for i in range(n):
    result = sys.stdin.readline().split()
    if result[0] == 'push':
        stack.append(result[1])
    if result[0] == 'pop':
        if not stack:
            answer.append(-1)
        else:
            answer.append(stack.pop())
    if result[0] == 'size':
        answer.append(len(stack))
    if result[0] == 'empty':
        if not stack:
            answer.append(1)
        else:
            answer.append(0)
    if result[0] == 'top':
        if not stack:
            answer.append(-1)
        else:
            answer.append(stack[-1])

for e in answer:
    print(e)
