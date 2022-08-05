
def main():
    N = int(input())

    results = [0] * N

    A = list(map(int, input().split()))
    
    B = []

    for a in enumerate(A):
        B.append(a)
    
    B.sort(key=lambda x : x[1])

    for i, x in enumerate(B):
        results[x[0]] = i

    for result in results:
        print(result, end=" ")

if __name__ == "__main__":
    main()