from math import gcd

def lcm(x, y):
    return x*y // gcd(x, y)

A, B = map(int, input().split())

print(gcd(A, B))

print(lcm(A, B))