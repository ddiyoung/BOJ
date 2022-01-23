def main():
    N = int(input())

    fibonacci = [0, 1, 1]

    for i in range(3, 41):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    for i in range(N):
        T = int(input())

        if T == 0:
            print("1 0")
        elif T == 1:
            print("0 1")
        else:
            print(fibonacci[T-1], fibonacci[T])


if __name__ == "__main__":
    main()
