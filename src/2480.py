def main():
    noon = input().split()

    for j in range(len(noon)):
        noon[j] = int(noon[j])

    tmp_noon = set(noon)

    if len(tmp_noon) == 1:
        result = 10000 + int(noon[0]) * 1000
    elif len(tmp_noon) == 2:
        for t in tmp_noon:
            if noon.count(t) == 2:
                result = 1000 + t * 100
    else :
        result = max(noon) * 100

    print(result)



if __name__ == "__main__":
    main()