def measure(n):
    
    measure_list = []

    for i in range(1, n):
        if n % i == 0:
            measure_list.append(i)

    return measure_list

def is_perfect(n):
    measure_list = measure(n)

    if n == sum(measure_list):
        print("%d = " %n, end ='')
        print(*measure_list, sep=' + ')
    else:
        print("%d is NOT perfect." %n)

def main():
    while True:
        n = int(input())
        
        if n == -1 :
            break
        
        is_perfect(n)


if __name__ == "__main__":
    main()