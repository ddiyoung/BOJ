from collections import deque

def bfs(dic):
    visited = set()
    que = deque([1])

    while que:
        n = que.popleft()

        if n not in visited:
            visited.add(n)
            que += dic[n] - visited
        
    visited.discard(1)

    return len(visited)


def main():
    N = int(input())

    dic = dict((i, set()) for i in range(1, N+1))

    M = int(input())

    for _ in range(M):
        a, b = map(int, input().split())

        dic[a].add(b)
        dic[b].add(a)
    print(bfs(dic))


if __name__ == "__main__":
    main()