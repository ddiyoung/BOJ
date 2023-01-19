def main():
    N = int(input())

    dp = [0 for _ in range(12)]

    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, 12):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    for _ in range(N):
        M = int(input())
        print(dp[M-1])

if __name__ == "__main__":
    main()