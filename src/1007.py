from itertools import combinations
import math

def main():
    results = []

    T = int(input())

    for _ in range(T):
        N = int(input())

        x_total = 0
        y_total = 0

        vertex = []
        for _ in range(N):
            x, y = map(int, input().split())
            x_total += x
            y_total += y
            vertex.append([x,y])
        
        comb = list(combinations(vertex, int(N/2)))

        min_len = math.inf

        for vector_sum in comb[:int(len(comb)/2)]:
            vector_sum = list(vector_sum)

            x1_total = 0
            y1_total = 0
            for x1, y1 in vector_sum:
                x1_total += x1
                y1_total += y1
            
            x2_total = x_total - x1_total
            y2_total = y_total - y1_total

            vector_len = math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2)

            min_len = min(min_len, vector_len)
        
        results.append(min_len)

    for result in results:
        print(result)
        

if __name__ == "__main__":
    main()
