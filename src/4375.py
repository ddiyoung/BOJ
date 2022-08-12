def main():
    while True:
        result = '1'

        try:
            n = int(input())
        except:
            break

        while True:
            if int(result) % n == 0:
                print(len(result))
                break
            result += '1'

if __name__ == "__main__":
    main()