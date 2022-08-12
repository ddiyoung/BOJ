def main():
    string = input()

    if string == string[::-1]:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()