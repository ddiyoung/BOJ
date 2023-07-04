import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    op = sys.stdin.readline().split()
    
    if op[0] == "push":
        stack.append(int(op[1]))
    elif op[0] == "pop":
        if stack:
            print(stack.pop())
        else :
            print(-1)
    elif op[0] == "size":
        print(len(stack))
    elif op[0] == "empty":
        if stack :
            print(0)
        else :
            print(1)
    elif op[0] == "top":
        if stack:
            print(stack[-1])
        else :
            print(-1)
