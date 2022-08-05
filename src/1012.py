def find_adj(MN, y, x, M, N):
    MN[y][x] = -1
    que = []

    que.append((y, x))

    while len(que) != 0 :
        bfs_y, bfs_x = que.pop(0)

        if bfs_x >= 1 :
            if MN[bfs_y][bfs_x-1] == 1:
                MN[bfs_y][bfs_x-1] = -1
                que.append((bfs_y, bfs_x - 1))
        if bfs_y >= 1:
            if MN[bfs_y-1][bfs_x] == 1:
                MN[bfs_y-1][bfs_x] = -1
                que.append((bfs_y-1, bfs_x))
        if bfs_x + 1 < M:
            if MN[bfs_y][bfs_x + 1] == 1:
                MN[bfs_y][bfs_x+1] = -1
                que.append((bfs_y, bfs_x+1))
        if bfs_y + 1 < N:
            if MN[bfs_y+1][bfs_x] == 1:
                MN[bfs_y+1][bfs_x] = -1
                que.append((bfs_y+1, bfs_x))      

    return MN 

def main():
    results = []

    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())

        MN = [[ 0 for _ in range(M)] for _ in range(N)]

        cnt = 0

        for _ in range(K):
            x, y = map(int, input().split())
            MN[y][x] = 1

        
        for y in range(N):
            for x in range(M):
                if MN[y][x] == 1:
                    cnt += 1
                    MN = find_adj(MN, y, x, M, N)

        results.append(cnt)        

    for result in results:
        print(result)

if __name__ == "__main__":
    main()