import math

def main():
    min, max = map(int, input().split())

    cnt = max - min + 1

    sqr = [False] * (max - min + 1)

    for i in range(2, int(max ** 0.5 + 1)):
        Square = i ** 2

        start = (((min - 1) // Square) + 1)*Square

        for j in range(start, max+1, Square):
            if not sqr[j-min]:
                sqr[j-min] = True
                cnt -= 1

    print(cnt)


if __name__ == "__main__":
    main()