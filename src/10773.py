import sys

K = int(sys.stdin.readline())

stack = []

for _ in range(K):
    money = int(sys.stdin.readline())
    
    if money:
        stack.append(money)
    else:
        stack.pop()
    
print(sum(stack))