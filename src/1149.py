def main():

    N = int(input())
    
    dp = [[0 for _ in range(3)] for _ in range(N+1)]
    
    rgb = list(map(int, input().split()))
    
    dp[0] = rgb
    
    for i in range(1, N):
        rgb = list(map(int, input().split()))
        
        dp[i][0] = rgb[0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = rgb[1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = rgb[2] + min(dp[i-1][0], dp[i-1][1])
    
    print(min(dp[N-1]))
        
            
if __name__ == "__main__":
    main()

