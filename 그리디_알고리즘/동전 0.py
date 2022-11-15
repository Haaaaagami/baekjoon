# https://www.acmicpc.net/problem/11047
# 그리디 알고리즘 실버 4 문제
# 22.10.29 시작
from sys import stdin

n, k = map(int, stdin.readline().split())
values = [int(stdin.readline()) for i in range(n)]
coin = 0

values.reverse()
for i in values:
    while k >= i:
        coin += k // i
        k %= i

print(coin)

