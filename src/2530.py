def main():
    A, B, C = map(int, input().split())

    D = int(input())

    C += D

    if C >= 60:
        tmp_C = C // 60
        C = C % 60
        B += tmp_C
    
    if B >= 60:
        tmp_B = B // 60
        B = B % 60
        A += tmp_B
    
    A = A % 24

    print(A, B, C)

if __name__ == "__main__":
    main()