# https://www.acmicpc.net/problem/3273
# 투포인터 실버 3 문제
# 11월 15일 시작

import heapq
from sys import stdin

n = int(stdin.readline())
nums = sorted(list(map(int, (stdin.readline().split()))))
x = int(stdin.readline())
cnt = 0
for i in range(n):
    target = x - nums[i]
    for j in range(i+1, n):
        if nums[j] == target:
            cnt += 1
        elif nums[j] > target:
            break

print(nums)

### 시간초과!

