def main():
    N = int(input())

    I = []

    for _ in range(N):
        i = tuple(map(int, input().split()))
        I.append(i)

    I.sort(key = lambda x : (x[1], x[0]))
    
    max_cnt = 1
    start = I[0]

    for i in range(1, N):
        if start[1] <= I[i][0]:
            max_cnt += 1
            start = I[i]
    
    print(max_cnt)


if __name__ == "__main__":
    main()