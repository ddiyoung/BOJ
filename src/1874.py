def print_ans(ans):
    for result in ans:
        print(result)

def main():
    stack = [1]
    
    N = int(input())
    
    seq = []
    
    for _ in range(N):
        val = int(input())
        
        seq.append(val)
    
    ans = ["+"]
    
    elem = 2
    
    cnt = 0
    
    while elem <= N :
        while seq[cnt] >= elem:
            stack.append(elem)
            elem += 1
            ans.append("+")
        
        while seq[cnt] <= elem - 1:
            if seq[cnt] < stack[-1]:
                print("NO")
                return  
            stack.pop()
            cnt += 1
            ans.append("-")
            if cnt == N-1:
                break
        
    while len(stack) != 0:
        stack.pop()
        ans.append("-")
        
    print_ans(ans)
    
    
if __name__ == "__main__":
    main()