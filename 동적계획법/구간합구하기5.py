# https://www.acmicpc.net/problem/11660
# 동적계획법 실버 1문제
# 22년 11월 11일 시작
# from sys import stdin
# n, m = map(int, stdin.readline().split())
# grp = [list(map(int, stdin.readline().split())) for _ in range(n)]
#
# cord = [list(map(int, stdin.readline().split()))for _ in range(m)]
#
# for i in range(n):
#     if i > 0:
#         grp[i][0] += grp[i-1][-1]
#     for j in range(1, n):
#         grp[i][j] += grp[i][j-1]
#
# for x1, y1, x2, y2 in cord:
#     if (x1, y1) == (x2, y2):
#         if x1 and y1 == 1:
#             print(grp[0][0])
#         else:
#             print(grp[x1-1][y1-1] - grp[x1-1][y1-2]) if y1 > 1 else print(grp[x1-1][y1-1] - grp[x1-2][-1])
#     else:
#         print(grp[x2-1][y2-1] - grp[x1-1][y1-1])

