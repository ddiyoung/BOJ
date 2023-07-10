import sys

N = int(sys.stdin.readline())

A = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().split()))

for x in B:
    if x in A:
        print(1)
    else:
        print(0)