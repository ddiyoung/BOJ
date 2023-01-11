def main():
    N = int(input())

    dis = list(map(int, input().split()))
    pay = list(map(int, input().split()))

    now_pay = pay[0]

    crt_pay = 0
    dis_pay = 0
    for i in range(1, N):
        dis_pay += dis[i-1]
        if pay[i] <= now_pay:
            crt_pay += now_pay * dis_pay            
            dis_pay = 0
            now_pay = pay[i]
    if dis_pay:
        crt_pay += now_pay * dis_pay

    
    print(crt_pay)

if __name__ == "__main__":
    main()