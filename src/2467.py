import sys
N = int(input())

liquid = list(map(int, input().split()))

target = sys.maxsize

left = 0
right = N - 1

answerL = 0
answerR = 0

while left < right:
    _sum = liquid[left] + liquid[right]

    if abs(_sum) < target:
        answerL = left
        answerR = right
        target = abs(_sum)
    
    if _sum > 0:
        right -= 1
    elif _sum < 0:
        left += 1
    else:
        break
        

print(liquid[answerL], liquid[answerR])

