def main():
    N = int(input())
    
    for _ in range(N):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        
        dis = r1 + r2
        dis_minus = abs(r1 - r2)
        
        x_dis = (x1-x2)**2
        y_dis = (y1-y2)**2
        
        O1toO2 = (x_dis + y_dis) ** 0.5
        
        if O1toO2 == 0 and r1 == r2:
            print(-1)
        elif dis_minus < O1toO2 < dis:
            print(2)
        elif dis == O1toO2 or dis_minus == O1toO2:
            print(1)
        elif O1toO2 > dis or O1toO2 < dis_minus:
            print(0)
        
if __name__ == "__main__":
    main()