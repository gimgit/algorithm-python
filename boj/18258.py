import sys
from collections import deque
sys.stdin = open('18258.txt')
input = sys.stdin.readline
n = int(input())


stack = deque([])
answer = []

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    if order[0] == 'pop':
        if not stack:
            answer.append(-1)
        else:
            answer.append(stack.popleft())
    if order[0] == 'size':
        answer.append(len(stack))
    if order[0] == 'empty':
        if not stack:
            answer.append(1)
        else:
            answer.append(0)
    if order[0] == 'front':
        if not stack:
            answer.append(-1)
        else:
            answer.append(stack[0])
    if order[0] == 'back':
        if not stack:
            answer.append(-1)
        else:
            answer.append(stack[-1])

for e in answer:
    print(e)
