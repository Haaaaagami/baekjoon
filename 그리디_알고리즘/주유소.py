# https://www.acmicpc.net/problem/13305
# 그리디 알고리즘 실버 3 문제
# 22.10.31 시작

from sys import stdin

n = int(stdin.readline())
road = list(map(int, stdin.readline().split()))
gas_fee = list(map(int, stdin.readline().split()))



total_gas_fee = 0
i = 0
while i < len(gas_fee)-1:
    total_length = 0
    
