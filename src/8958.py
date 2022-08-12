def main():
    T = int(input())

    for _ in range(T):
        string = input()

        score = 0

        continue_cnt = 1

        for result in string:
            if result == "O":
                score += continue_cnt
                continue_cnt += 1
            else :
                continue_cnt = 1
        
        print(score)
            

if __name__ == "__main__":
    main()