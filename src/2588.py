def main():
    A = int(input())
    B = int(input())

    _3_ = A * (B % 10)
    _4_ = A * ((B // 10) % 10)
    _5_ = A * ((B // 100) % 10)
    _6_ = A * B

    print(_3_)
    print(_4_)
    print(_5_)
    print(_6_)

if __name__ == "__main__":
    main()