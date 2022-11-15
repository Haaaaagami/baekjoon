def bdg(n):
    result = []
    result.extend([0, 1, 0, 1])
    result.extend([0] * (n+1))
    result.extend([1] * (n+1))
    return result
game = []
for i in range(1, 300):
    game.extend(bdg(i))

A = int(input())
T = int(input())
bd = int(input())

cnt = 0
result = 0
for i in range(len(game)):
    if game[i] == bd:
        cnt += 1
    if cnt == T:
        result = i


result = result % (A-1)
print(result)
