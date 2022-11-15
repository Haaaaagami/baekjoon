# https://www.acmicpc.net/problem/1912
# 동적 계획법 실버 2 문제
# 22.10.29 시작
#1. 주어진 수열에서 연속하는 양수끼리, 연속하는 음수끼리 더한 수열을 만든다.
#2. 1.에서 만들어진 수열의 길이만큼 for 문을 실행하는데, i번째 요소가 양수라면, [i+1] + [i+2] 가 양수인지 확인하여 양수라면 [i]번째 요소에 더하고,
#     [i+3] + [i+4] 에 대해서도 양수라면 [i]번째 요소에 더하고 ---> 음수일때까지 반복한다
#3. [i+N] + [i+N+1]이 음수라면, [i+N]을 결과 리스트에 더하고
#4. [i+N+1]에 대해 2~3의 과정을 거친다.
#5. 4의 과정이 끝난 결과 리스트에 대해 2~4의 과정을 리스트의 요소가 2개 이하로 남을때 까지 거친다.
#6. 리스트의 요소가 2개중 양수인 쪽이 정답이다.


import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
dp = []


# 주어진 수열에서 양수, 음수를 묶은 수열 생성, 양끝이 음수라면 삭제
i = 1
sum_ = n_list[0]
while i < len(n_list):
    while (n_list[i] ^ n_list[i-1]) >= 0:
        sum_ += n_list[i]
        i += 1
    proc_list.append(sum_)
    sum_ = n_list[i]
    i += 1


# 실패!
