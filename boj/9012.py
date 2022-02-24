import sys
sys.stdin = open('9012.txt')
T = int(sys.stdin.readline())
for i in range(T):
    stack = list(input())

    while len(stack) != 0:
        if stack[0] == ")":
            print('NO')
            break
        else:
            if ')' in stack:
                stack.remove(')')
                stack.remove('(')
            else:
                print("NO")
                break
    if len(stack) == 0:
        print("YES")

# input
# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(
