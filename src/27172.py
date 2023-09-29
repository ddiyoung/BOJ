import sys

N = int(sys.stdin.readline())

result = [-1] * 1000001

card = list(map(int, sys.stdin.readline().split()))

for num in card:
    result[num] = 0

sort_card = sorted(card)

for num in sort_card:
    for i in range(1, int(1000001 / num)+1):
        if num * i < 1000001:
            if result[num * i] >= 0:
                result[num] -= 1
                result[num * i] += 1

for num in card:
    print(result[num] * -1, end=" ")
print()