def main():
    N = int(input())
    
    pages = [0 for i in range(10)]
    
    point = 1
    
    while N != 0:
        while N % 10 != 9:
            for i in str(N):
                pages[int(i)] += point
            N -= 1
        
        if N < 10:
            for i in range(N+1):
                pages[i] += point
            pages[0] -= point
            break
        else:
            for i in range(10):
                pages[i] += (N // 10 + 1) * point
        pages[0] -= point
        point *= 10
        N //= 10
                
    
    for page in pages:
        print(page, end=" ")
        
    print()
    

if __name__ == "__main__":
    main()