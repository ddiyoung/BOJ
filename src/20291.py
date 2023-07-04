import sys

N = int(sys.stdin.readline())

dic = dict()

for _ in range(N):
    file = input().split('.')
    if file[1] in dic:
        dic[file[1]] += 1
    else:
        dic[file[1]] = 1

keys = list(dic.keys())

keys.sort()

for key in keys:
    print(key, dic[key])