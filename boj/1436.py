import sys

sys.stdin = open('1436.txt')
input = sys.stdin.readline


n = int(input())
c = 0
t = 666

while c < n:
    if '666' in str(t):
        c += 1
    t += 1


print(t - 1)
