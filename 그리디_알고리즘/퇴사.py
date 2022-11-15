# https://www.acmicpc.net/problem/14501
# 그리디 알고리즘 실버 3문제
# 22년 11월 10일

# n = int(input())
# coun = [tuple(map(int, input().split())) for i in range(n)]
#
# print(coun)
#
# day = 0
# money = 0
# while i < n:
#     if coun[day][0] == 1:
#         money += coun[day][1]
#         day += 1
#     else:
#         for j in coun[day: day + coun[day] -1]:
#             if j
from sys import stdin

asc = '1 2 3 4 5 6 7 8'
desc = '8 7 6 5 4 3 2 1'
inp = input()
if inp == asc:
    print('ascending')
elif inp == desc:
    print('descending')
else:
    print('mixed')