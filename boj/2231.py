import sys

sys.stdin = open('2231.txt')
input = sys.stdin.readline

# 인풋 = 216 000 + 9 + 9 + 9
# 3자리수 9와 9와 9
# 9,9,9 => 27 + ??? => 216
# 216-27
# 189~216

a = input()
b = 9*(len(a))  # 분해합의 자릿수 * 9
k = int(a)
for i in range(k-b, k):
    c = str(i)  # 각 자릿수의 숫자를 꺼내오기 위해서 string으로 형변환 한다.
    d = i  # d를 검사하는 숫자로 할당
    for e in c:
        if e != '-':  # 분해합의 숫자가 9보다 작으면 음수가 나올 수 있다.
            d += int(e)  # 미리 검사하는 숫자로 할당한 d에서 각 자릿수를 또 더해준다.
    if d == k:
        print(i)
        break
else:
    print(0)  # break로 나오면 실행하지 않는다.
