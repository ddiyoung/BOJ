def main():
    A, B = map(int, input().split())

    C = int(input())

    B = B + C

    if B >= 60:
        tmp_A = B // 60
        B = B % 60
        A += tmp_A
    

    if A >= 24:
        A = A % 24
    
    print(A, B)


if __name__ == "__main__":
    main()