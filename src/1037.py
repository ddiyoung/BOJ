def main():
    cnt = int(input())

    real = list(map(int, input().split()))

    print(max(real) * min(real))



if __name__ == "__main__":
    main()