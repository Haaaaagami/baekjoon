# https://www.acmicpc.net/problem/1904
# 동적 계획법 실버 3 문제
# 22.10.27 시작

k = int(input())
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
for i in range(3, k+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[k])
