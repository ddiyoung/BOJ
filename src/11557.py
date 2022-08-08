def main():
    T = int(input())

    for _ in range(T):
        N = int(input())

        school = []
        L = []

        for _ in range(N):
            name, liter = input().split()
            liter = int(liter)

            school.append(name)
            L.append(liter)

        print(school[L.index(max(L))])



if __name__ == "__main__":
    main()