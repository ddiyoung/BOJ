def main():
    N = int(input())

    not_cute = 0
    cute = 0

    for _ in range(N):
        vote = int(input())
        
        if vote == 1:
            cute += 1
        elif vote == 0:
            not_cute += 1
    
    if cute > not_cute:
        print("Junhee is cute!")
    elif not_cute > cute:
        print("Junhee is not cute!")

if __name__ == "__main__":
    main()