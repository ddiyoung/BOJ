def main():
    N = int(input())

    fac = 1

    for i in range(2, N+1):
        fac *= i
    
    string = str(fac)
    string = string[::-1]

    cnt = 0

    for s in string:
        if s != '0':
            print(cnt)
            return
        cnt += 1



if __name__ == "__main__":
    main()