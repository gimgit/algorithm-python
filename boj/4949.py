import sys

sys.stdin = open('4949.txt')
input = sys.stdin.readline
print(input)

while True:
    s = input().rstrip()
    if s == '.':
        break
    # 입력의 종료 조건 점하나 있을때

    stack = []
    flag = True
    loop = len(s)
    for i in range(loop):
        if not stack and s[i] in '])':
            flag = False
            break

        elif s[i] in '([':
            stack.append(s[i])

        elif stack and s[i] in ')]':  # stack은 있고 닫힌 괄호가 나오는 경우
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break

    if flag is True and not stack:
        print('yes')
    else:
        print('no')
