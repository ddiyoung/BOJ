def main():
    N = int(input())
    
    s = 2

    while N != 1:
        if N % s == 0:
            N = N // s
            print(s)
        else:
            s += 1
    

if __name__ == "__main__":
    main()