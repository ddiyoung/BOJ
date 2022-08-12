def main():
    T = int(input())

    for _ in range(T):
        r, e, c = map(int, input().split())

        adv = e - c

        if r < adv :
            print("advertise")
        elif r > adv :
            print("do not advertise")
        else :
            print("does not matter")


if __name__ == "__main__":
    main()