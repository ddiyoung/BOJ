def main():
    N = int(input())

    cnt = [0] * 5

    for _ in range(N):
        x, y = map(int, input().split())

        if x == 0 or y == 0 :
            cnt[4] += 1
        elif x > 0 and y > 0 :
            cnt[0] += 1
        elif x < 0 and y > 0 :
            cnt[1] += 1
        elif x < 0 and y < 0 :
            cnt[2] += 1
        elif x > 0 and y < 0 :
            cnt[3] += 1

    result = """Q1: %d
Q2: %d
Q3: %d
Q4: %d
AXIS: %d"""
    
    print(result %(tuple([i for i in cnt])))

if __name__ == "__main__":
    main()