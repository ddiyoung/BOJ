def main():
    N = int(input())

    rope = []

    for _ in range(N):
        rope.append(int(input()))
    
    rope.sort(reverse=True)

    max = 0

    for i in range(len(rope)):
        tmp = rope[i] * (i + 1)
        if max < tmp:
            max = tmp
        
    print(max)

if __name__ == "__main__":
    main()