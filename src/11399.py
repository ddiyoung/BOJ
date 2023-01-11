def main():
    N = int(input())

    ans = 0

    P = input().split()

    for i in range(len(P)):
        P[i] = int(P[i])

    P.sort()

    for i in range(len(P) - 1):
        ans += P[i]
        P[i+1] += P[i]
    
    ans += P[N-1]
    print(ans)

if __name__ == "__main__":
    main()