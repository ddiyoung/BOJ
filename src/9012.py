import sys

def push_pop(string, stack):
    for ps in string:
        if ps == "(":
            stack.append(ps)
        else:
            if len(stack):
                stack.pop()
            else:
                print("NO")
                return
    if not len(stack):
        print("YES")
        return
    else:
        print("NO")
        return

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    string = sys.stdin.readline().rstrip()
    
    push_pop(string, stack)
