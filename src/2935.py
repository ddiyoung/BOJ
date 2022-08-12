def main():
    A = int(input())
    op = input()
    B = int(input())

    if op == "*":
        result = A * B
    elif op == "+":
        result = A + B

    print(result)

if __name__ == "__main__":
    main()