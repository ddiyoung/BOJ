def main():
    H, M = map(int, input().split())

    M = M - 45

    if M < 0:
        M = 60 + M
        H -= 1
    
    if H < 0:
        H = 24 + H

    print(H, M)

if __name__ == "__main__":
    main()