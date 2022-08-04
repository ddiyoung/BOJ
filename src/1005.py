class Graph:
    #그래프
    def __init__(self, n):
        self.G = dict(zip([i for i in range(1, n+1)], [[] for _ in range(n)]))

    def add(self, src, dst):
        self.G[src].append(dst)
    

def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())

        graph = Graph(N) #N개의 정점을 가지는 그래프 생성

        D = list(map(int, input().split()))

        for _ in range(K): #Edges의 개수 만큼 반복
            src, dst = map(int, input().split())
            graph.add(src, dst)

        print(graph.G)

        W = int(input())

if __name__ == "__main__":
    main()
