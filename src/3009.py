def find_one(L):
    for point in L:
        if L.count(point) == 1:
            return point

def main():
    x_list = []
    y_list = []
    for _ in range(3):
        x, y = map(int, input().split())

        x_list.append(x)
        y_list.append(y)

    
    x = find_one(x_list)
    y = find_one(y_list)

    print(x, y)
    
if __name__ == "__main__":
    main()