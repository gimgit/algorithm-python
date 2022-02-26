import sys
sys.stdin = open('10773.txt')
input = sys.stdin.readline
n = int(input())


stack = []
for i in range(n):
    result = int(input())
    if result == 0:
        stack.pop()
    else:
        stack.append(result)


print(sum(stack))
