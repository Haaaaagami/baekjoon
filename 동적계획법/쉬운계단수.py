# https://www.acmicpc.net/problem/10844
# 동적 계획법 실버 1 문제
# 2022.11.1 시작

def dp(n):
    if n < 2:
        return 9
    else:
        for i in range(2, n+1):
            save[i] = (save[i-1] * 2 - i + 1) % 1000000000
        return save[n]


save = [0 for _ in range(101)]
save[1] = 9
print(dp(int(input())))

