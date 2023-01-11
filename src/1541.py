def main():
    string = input().split('-')
    
    num = []

    for idx, val in enumerate(string):
        operate = val.split('+')
        val_sum = 0
        for op in operate:
            val_sum += int(op)
        
        num.append(val_sum)
    
    result = num[0]

    for i in range(1, len(num)):
        result -= num[i]
    
    print(result)


if __name__ == "__main__":
    main()