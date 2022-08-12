def main():
    T = int(input())

    results = []

    for _ in range(T):
        RS = input().split()

        result = ""
        for s in RS[1]:
            result += s * int(RS[0])

        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()