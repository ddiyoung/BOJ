N, M = map(int, input().split())

Dict = dict()

cnt = 0

for _ in range(N):
    name = input()
    Dict[name] = 0

for _ in range(M):
    name = input()
    if name in Dict:
        Dict[name] = 1
        cnt += 1

print(cnt)

for key in sorted(Dict):
    if Dict[key] == 1:
        print(key)