import sys

front_stack = list(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline())

back_stack = []


for _ in range(M):
    op = sys.stdin.readline().split()
    
    if op[0] == "L" and front_stack:
        back_stack.append(front_stack.pop())
    elif op[0] == "D" and back_stack:
        front_stack.append(back_stack.pop())
    elif op[0] == "B" and front_stack:
        front_stack.pop()
    elif op[0] == "P":
        front_stack.append(op[1])

front_stack.extend(reversed(back_stack))
        
print(''.join(front_stack))
