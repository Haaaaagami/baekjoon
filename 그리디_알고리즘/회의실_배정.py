# https://www.acmicpc.net/problem/1931
# 그리디 알고리즘 실버 1 문제
# 22.10.29 시작

from sys import stdin
n = int(stdin.readline())
lec_list = []
for i in range(n):
    tub = tuple(map(int, stdin.readline().split()))
    lec_list.append(tub)

lec_list = sorted(lec_list, key=lambda x: (x[1], x[0])) # <<< 1 0, 0 1 을 주면 1이나오는 오류가 있어 두번째 정렬조건으로 x[0] 추가
num = 1
i = 0
end_time = lec_list[0][1]

for i in range(1, len(lec_list)):
    if lec_list[i][0] >= end_time:
        num += 1
        end_time = lec_list[i][1]

print(num)