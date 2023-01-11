def main():
    N = input()

    present = 0

    for num in N:
        present += int(num)
    
    if present % 3 != 0 or not ('0' in N):
        print(-1)
        return
    
    uniq = list(N)
    uniq.sort(reverse = True)

    result = ''.join(num for num in uniq)

    print(result)

if __name__ == "__main__":
    main()