def main():
    T = int(input())

    results = []

    for _ in range(T):
        operate = input().split()

        result = float(operate[0])

        for op in operate:
            if op == "@":
                result *= 3
            elif op == "%":
                result += 5
            elif op == "#":
                result -= 7
            
        results.append(result)
    
    for result in results:
        print("%.2f" %result)


if __name__ == "__main__":
    main()