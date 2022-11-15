money1 = [0, 500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
money2 = [0, 512, 256, 256, 128, 128, 128, 128]
money2.extend([64] * 8)
money2.extend([32] * 16)
money1.extend([0 for _ in range(100)])
money2.extend([0 for _ in range(100)])
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print((money1[a] + money2[b]) * 10000)