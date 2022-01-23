def main():
    T = int(input())
    for j in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())

        cnt = 0

        for i in range(n):
            cx, cy, r = map(int, input().split())
            d1 = ((x1-cx)**2 + (y1-cy)**2) ** 0.5
            d2 = ((x2-cx)**2 + (y2-cy)**2) ** 0.5
            # is it in circle?
            if d1 < r and d2 > r:
                cnt += 1
            elif d1 > r and d2 < r:
                cnt += 1

        print(cnt)


if __name__ == "__main__":
    main()
