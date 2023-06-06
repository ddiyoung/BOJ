def multi(A, B, C):
    if B == 1:
        return A % C
    else :
        tmp = multi(A, B//2, C)
        if B % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C
    

def main():
    
    A, B, C = map(int, input().split())
    
    print(multi(A,B,C))
    
            
if __name__ == "__main__":
    main()

