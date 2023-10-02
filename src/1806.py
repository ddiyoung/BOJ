import sys

N, S = map(int, sys.stdin.readline().split())

sequence = list(map(int, sys.stdin.readline().split()))

i, j = 0, 0

min_len = N+1

sub_sum = 0

while True:
    if sub_sum >= S:
        min_len = min(min_len, j - i)
        sub_sum -= sequence[i]
        i += 1
    elif j >= N:
        break
    else:
        sub_sum += sequence[j]
        j += 1

if min_len == N+1:
    print(0)
else:
    print(min_len)