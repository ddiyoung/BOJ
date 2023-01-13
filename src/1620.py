N, M = map(int, input().split())

Dict_name = dict()
name_list = list()

for i in range(1, N+1):
    name = input()
    Dict_name[name] = i
    name_list.append(name)

for _ in range(M):
    quiz = input()

    if quiz.isdigit():
        print(name_list[int(quiz) - 1])
    else:
        print(Dict_name[quiz])