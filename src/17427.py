def main():

    N = int(input())

    result = 0

    for a in range(1, N+1):
        result += a*(N // a)

    print(result)
    
if __name__ == "__main__":
    main()