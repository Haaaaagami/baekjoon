# https://www.acmicpc.net/problem/20300
# 그리디알고리즘 실버 3 문제
from sys import stdin

n = int(stdin.readline())
nums = sorted(list(map(int, stdin.readline().split())))
ans = []
if len(nums) % 2:
    ans.append(nums[-1])
    for i in range(len(nums)//2):
        ans.append(nums[i] + nums[-(i+2)])
else:
    for i in range(len(nums)//2):
        ans.append(nums[i] + nums[-(i+1)])

print(max(ans))