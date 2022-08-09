from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    T = int(input())

    for _ in range(T):
        A, B = map(int, input().split())

        print(lcm(A, B))
        


if __name__ == "__main__":
    main()