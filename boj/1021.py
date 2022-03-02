from collections import deque
import sys

sys.stdin = open('1021.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
dq = deque([i for i in range(1, n+1)])
position = list(map(int, input().split()))

# print(position)  # 뽑아올 숫자
count = 0
while position:
    if dq[0] == position[0]:
        dq.popleft()
        del position[0]
    else:
        if dq.index(position[0]) < len(dq)/2:
            while dq[0] != position[0]:
                dq.append(dq.popleft())
                count += 1
        else:
            while dq[0] != position[0]:
                dq.appendleft(dq.pop())
                count += 1
print(count)
