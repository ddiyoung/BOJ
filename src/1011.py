import math

def main():
    results = []

    T = int(input())

    for _ in range(T):
        x, y = map(int, input().split())

        distance = y - x

        N_distance = int(distance - 0.5)

        N = int((-1 + math.sqrt(1+4 * N_distance)) / 2)

        N_N = N * (N+1)

        if distance <= (N_N + 1 + N):
            result = N * 2 + 1
        else :
            result = N * 2 + 2

        results.append(result)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()