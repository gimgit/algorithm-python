import sys
sys.stdin = open('input.txt')
T = int(sys.stdin.readline())
for i in range(T):
    stack = list(sys.stdin.readline().rstrip())
    sum = 0
    for target in stack:
        if target == '(':
            sum += 1
        elif target == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum == 0:
        print("Yes")
    else:
        print("NO")
        
        
# input       
# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(
