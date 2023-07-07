import sys
sys.setrecursionlimit(1000000)
N, M = map(int, sys.stdin.readline().split())

parent = [elem for elem in range(N+1)]

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
for _ in range(M):
    op, a, b = map(int, sys.stdin.readline().split())
    if op:
        if find(a) == find(b):
            print("YES")
        else :
            print("NO")
    else:
        union(a, b)