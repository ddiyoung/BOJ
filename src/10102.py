def main():
    V = int(input())

    votes = input()

    A = 0
    B = 0

    for vote in votes:
        if vote == "A":
            A +=1
        elif vote == "B":
            B +=1

    if A > B:
        print("A")
    elif B > A :
        print("B")
    else:
        print("Tie")

if __name__ == "__main__":
    main()