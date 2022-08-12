def main():
    T = int(input())

    for _ in range(T):
        Yonsei , Korea = 0, 0

        for _ in range(9):
            y, k = map(int, input().split())

            Yonsei += y 
            Korea += k
        
        if Yonsei > Korea:
            result = "Yonsei"
        else:
            result = "Korea"

        print(result)

if __name__ == "__main__":
    main()