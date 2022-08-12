def main():
    n = int(input())

    score = [100, 100]

    for _ in range(n):
        A, B = map(int, input().split())

        if A > B:
            score[1] -= A
        elif A < B:
            score[0] -= B

    print(score[0])            
    print(score[1])


if __name__ == "__main__":
    main()