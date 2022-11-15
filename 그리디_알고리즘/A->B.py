# https://www.acmicpc.net/problem/16953
# 그리디 알고리즘 실버 2문제
# 22년 11월 7일 시작

a, b = map(int, input().split())
cnt = 1
while True:
    if a == b:
        print(-1)
        break

    if (b - 1) % 10:
        b /= 2
        cnt += 1
    else:
        b = (b - 1) / 10
        cnt += 1

    if b == a:
        print(cnt)
        break

    elif b < a:
        print(-1)
        break
