def main():
    change = [500, 100, 50, 10, 5, 1]

    value = int(input())

    value = 1000 - value

    ans = 0
    idx = 0
    while value > 0:
        ans += value // change[idx]
        value -= change[idx] * (value // change[idx])
        idx += 1
    
    print(ans)

if __name__ == "__main__":
    main()