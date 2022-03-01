import sys
import heapq

sys.stdin = open('1927.txt')
input = sys.stdin.readline
numbers = int(input())

heap = []


for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
