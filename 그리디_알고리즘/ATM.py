# https://www.acmicpc.net/problem/11399
# 그리디 알고리즘 실버 4 문제
# 22.10.30 시작

from sys import stdin
n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))

n_list.sort()
dp = [0 for _ in range(len(n_list))]
dp[0] = n_list[0]
for i in range(1, len(n_list)):
    dp[i] = dp[i-1] + n_list[i]

print(sum(dp))
