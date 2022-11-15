# https://www.acmicpc.net/problem/11000
# 그리디 알고리즘 골드 5문제

from sys import stdin
n = int(stdin.readline())
cls = [list(map(int, stdin.readline().split())) for i in range(n)]
cls = sorted(cls, key=lambda x:(x[1],x[0]))
print(cls)

ans = []
cnt = 0
while c:
    for i in range(len(cls)-1):
        if cls[i][0]:
            if cls[i][1] <= cls[i+1][0]:
                cls[i][0] = -1
    cnt += 1