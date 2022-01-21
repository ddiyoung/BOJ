from argparse import ONE_OR_MORE


def fibonacci(n):
    if n == 0:
        global zero 
        zero += 1
        return 0
    elif n == 1:
        global one
        one += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    N = int(input())

    global zero
    global one
    zero = 0
    one = 0

    for i in range(N):
        fibonacci(int(input()))
        print("%d %d" %(zero, one))
        zero = 0
        one = 0

if __name__ == "__main__":
    main()
