N = int(input())

stairs = []

for _ in range(N):
    score = int(input())

    stairs.append(score)

dp = [[0, 0] for _ in range(N+1)]

dp[1][0] = stairs[0]

for idx in range(2, N+1):
    dp[idx][0] = max(dp[idx-2]) + stairs[idx-1]
    dp[idx][1] = dp[idx-1][0] + stairs[idx-1]

print(max(dp[N]))
