N = int(input())

for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif d <= r1 or d <= r2:
        if abs(r2-r1) > d:
            print(0)
        elif abs(r2-r1) == d:
            print(1)
        else:
            print(2)
    else:
        if r2 + r1 > d:
            print(2)
        elif r2 + r1 == d:
            print(1)
        else:
            print(0)
