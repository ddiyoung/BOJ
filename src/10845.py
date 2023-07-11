import sys
from collections import deque

que = deque()

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        que.appendleft(command[1])
    elif command[0] == "pop":
        if len(que):
            print(que.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(que))
    elif command[0] == "empty":
        if len(que):
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if len(que):        
            print(que[-1])
        else:
            print(-1)
    elif command[0] == "back":
        if len(que):
            print(que[0])
        else:
            print(-1)