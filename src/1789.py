def main():
    S = int(input())

    N = (-1 + (1+8*S) ** 0.5) / 2
    
    print(int(N))

if __name__ == "__main__":
    main()