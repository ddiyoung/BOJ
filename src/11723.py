import sys
N = int(input())

S = set()
for _ in range(N):
    command = sys.stdin.readline().strip().split(' ')

    if len(command) == 1:
        if command[0] == 'all':
            All = [i for i in range(1, 21)]
            S = set(All)
        if command[0] == 'empty':
            S = set()
        continue
        
    if command[0] == 'add':
        S.add(int(command[1]))
    elif command[0] == 'remove':
        S.discard(int(command[1]))
    elif command[0] == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else :
            S.add(int(command[1]))

