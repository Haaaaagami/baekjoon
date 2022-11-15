# https://www.acmicpc.net/problem/20115
# 그리디 알고리즘 실버 3 문제
# 22.11.03 시작

from sys import stdin

n = int(stdin.readline())
energy_drink = list(map(int, stdin.readline().split()))
#리스트 정렬
energy_drink.sort()
# 가장 마지막에 있는 요소(가장 큰요소)에 1~i 까지의 합에 0.5를 곱해 더함
for i in range(len(energy_drink)-1):
    energy_drink[-1] += energy_drink[i] / 2

print(energy_drink[-1])