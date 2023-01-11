def main():
    N = int(input())

    ans = 0
    while N >= 0:
        if N % 5 == 0:
            ans += N // 5
            print(ans)
            return
        N -= 3
        ans += 1
    
    print(-1)

if __name__ == "__main__":
    main()