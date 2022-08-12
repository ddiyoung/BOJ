def main():

    score = []

    for _ in range(5):
        tmp = int(input())
        if tmp <= 40:
            tmp = 40
        score.append(tmp)

    avg = int(sum(score) / 5)

    print(avg)

if __name__ == "__main__":
    main()