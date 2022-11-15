# https://www.acmicpc.net/problem/2217
# 그리디 알고리즘 실버 4 문제
# 11월 12 일 시작

n = int(input())
ans = []
ropes = [int(input()) for _ in range(n)]
ropes.sort()
for i in range(n):
    ans.append(ropes[i] * (len(ropes) - i))

print(max(ans))