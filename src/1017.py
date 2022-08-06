from itertools import combinations

def isPrime(number):
    cnt = 0
    for i in range(2, number):
        if cnt > 0:
            break
        if number % i == 0:
            cnt += 1
    
    if cnt == 0:
        return True
    else:
        return False


def main():
    N = int(input())

    number = list(map(int, input().split()))

    results = []    

    for i in range(1, N):
        first = number[0] + number[i]

        if isPrime(first):
            b = number.copy()
            del b[i]
            del b[0]

            print(list(combinations(b, 2)))
        # if first is prime?
            # 다른 조합이 소수인 경우를 찾아준다.
                # 다른 조합이 모두 소우인 경우 results 배열에 number[i] 추가

    if len(results) == 0:
        print(-1)
    else:
        for result in results:
            print(result, end=" ")

if __name__ == "__main__":
    main()