import copy

n, m = map(int, input().split())
chess1 = [[0 if j == 'B' else 1 for j in input()] for _ in range(n)]
chess2 = copy.deepcopy(chess1)
cnt = 0
start = 0
ans = []
start = chess1[0][0]
for i in range(n):
    chess1[i][0] = start
    for j in range(m-1):
        if chess1[i][j] ^ chess1[i][j+1] == 0:
            chess1[i][j+1] = 0 if chess1[i][j] else 1
            cnt += 1
    start = 0 if chess1[i][0] else 1
ans.append(cnt)


cnt = 1
start = 0 if chess2[0][0] else 1
chess2[0][0] = 0 if chess2[0][0] else 1
for i in range(n):
    chess2[i][0] = start
    for j in range(m-1):
        if chess2[i][j] ^ chess2[i][j+1] == 0:
            chess2[i][j+1] = 0 if chess2[i][j] else 1
            cnt += 1
    start = 0 if chess2[i][0] else 1
ans.append(cnt)

print(min(ans))