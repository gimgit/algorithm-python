import sys
sys.stdin = open('11866.txt')
input = sys.stdin.readline

N, K = map(int, sys.stdin.readline().split())

queue = [i for i in range(1, N+1)]  # 리스트 컴프리헨션으로 1부터 N까지의 순열 생성
answer = []

while queue:    # 큐에 원소가 없을 때까지 반복하는 반복문
    for _ in range(K-1):
        tmp = queue.pop(0)    # 첫번째 원소를 pop하여 tmp 변수에 지정
        queue.append(tmp)  # 큐의 맨 뒤에 tmp를 append함
    dead = queue.pop(0)    # K번째에 위치한 원소를 제거하고 dead에 지정
    answer.append(dead)  # Josephus 리스트에 dead를 넣어줌

print('<'+', '.join(map(str, answer))+'>')


# n = input().split()
# num = int(n[0])
# target = int(n[1])
# # print(num, target)
# dq = deque([i for i in range(1, num+1)])
# # print(dq[0])
# answer = []
# # loop = len(dq) - target + 1
# # print(loop)


# while len(dq) >= target:
#     target_num = int(dq[target-1])

#     print(target_num, dq[0], dq)
#     for i in range(num):
#         if dq[0] == target_num:
#             answer.append(dq.popleft())
#         else:
#             print(dq)
#             dq.popleft()
#             dq.append(dq.popleft())

# print(answer)
