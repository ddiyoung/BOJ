import sys
from collections import deque



N = int(sys.stdin.readline())

que = deque([i for i in range(1, N+1)])

while len(que) != 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])