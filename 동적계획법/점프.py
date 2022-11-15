# https://www.acmicpc.net/problem/1890
# 동적계획법 실버 1문제
# 22년 11월 8일 시작
# 아이디어 - 게임판과 똑같이 생긴 판(정답판, ans) 을 만들어서 게임판에서 해당 좌표에 도착할 수 있는 경우의 수를 써놓고, 시작칸의 경우의 수를 도착칸에도 더해주는
# 작업을 오른쪽 아래 칸(도착지) 까지 하면, 정답판의 도착지의 좌표에( [-1][-1] ) 도착할 수 있는 경우의수가 저장된다.

import sys
n = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [[0 for _ in range(n)] for i in range(n)] # 정답판 만들기. 정적 배열을 사용하여 시간 줄임

# 시작칸에 도착할 수 있는 경우의 수는 시작할 때 뿐이므로 정답판의 첫 칸에 1 저장
ans[0][0] = 1
for i in range(n):
    for j in range(n):
        # 만약 거리가 0 이라면 해당 칸에서 움직이지 못함
        if game[i][j] == 0:
            continue
        # 우측으로 움직일 수 있다면 우측으로 거리만큼 이동하여 도착칸의 경우의 수에 출발칸의 경우의 수를 더함
        if j + game[i][j] < n:
            ans[i][j + game[i][j]] += ans[i][j]
        # 아래로 움직일 수 있다면 아래로 거리만큼 이동하여 도착칸의 경우의 수에 출발칸의 경우의 수를 더함
        if i + game[i][j] < n:
            ans[i + game[i][j]][j] += ans[i][j]
# 가장 우측 아래칸 출력
print(ans[-1][-1])