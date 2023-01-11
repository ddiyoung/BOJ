def main():
    N, K = map(int, input().split())

    A = []

    for _ in range(N):
        tmp = int(input())

        A.append(tmp)
    
    A.reverse()

    ans = 0

    for a in A:
        ans += K // a
        K = K % a
    
    print(ans)

if __name__ == "__main__":
    main()