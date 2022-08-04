class Graph:
    #그래프
    def __init__(self, N, D):
        self.N = N
        self.G = dict(zip([i for i in range(1, N+1)], [{'adj' : [], 'time': -1} for _ in range(N)]))
        self.D = D
    
    def print_graph(self):
        for i in range(1, self.N + 1):
            print(self.G[i])

    def add(self, src, dst):
        self.G[dst]['adj'].append(src)
    
    def init_time(self):
        for i in range(1, self.N + 1):
            if len(self.G[i]['adj']) == 0:
                self.G[i]['time'] = self.D[i-1]

    def cal(self, W):
        


def main():
    result = []
    
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())

        D = list(map(int, input().split()))

        graph = Graph(N, D) #N개의 정점을 가지는 그래프 생성

        for _ in range(K): #Edges의 개수 만큼 반복
            src, dst = map(int, input().split())
            graph.add(src, dst)

        graph.init_time()
        graph.print_graph()

        W = int(input())

        result.append(graph.G[W]['time'])

    print(result)

if __name__ == "__main__":
    main()
