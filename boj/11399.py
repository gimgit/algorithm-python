import sys
sys.stdin = open('11399.txt')
input = sys.stdin.readline
n = int(input())
m = list(map(int, input().split()))
m.sort()

process_time = [0 for _ in range(n)]
total_process_time = 0

for i in range(n):
    print(total_process_time)
    if i == 0:
        process_time[i] = m[0]
        total_process_time = m[0]
    else:
        process_time[i] = process_time[i-1] + m[i]
        total_process_time += process_time[i]

print(process_time)
