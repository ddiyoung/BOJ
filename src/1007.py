from itertools import combinations

def vector(tuple):
    v1 = tuple[0]
    v2 = tuple[1]

    if v1[0] < v2[0]:
        v1 = tuple[1]
        v2 = tuple[0]
    
    vector = [v1[0] - v2[0], v1[1] - v2[1]]
    return vector

def vectorlist(comb):
    vector_list = []
    for c in comb:
        vector_list.append(vector(c))
    
    return vector_list

def main():
    T = int(input())

    for _ in range(T):
        N = int(input())

        vertex = []
        for _ in range(N):
            x, y = map(int, input().split())
            vertex.append([x,y])
        
        comb = list(combinations(vertex, 2))

        vec = vectorlist(comb)

        print(vec)

if __name__ == "__main__":
    main()
