import datetime

def main():
    now = datetime.datetime.now()

    print("%04d-%02d-%02d" %(now.year, now.month, now.day))

if __name__ == "__main__":
    main()