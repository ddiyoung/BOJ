def main():
    N = input().split()

    for j in range(len(N)):
        N[j] = int(N[j])

    s = sum(N)
    m = max(N)
    n = min(N)

    result = s - m - n
    print(result)

if __name__ == "__main__":
    main()