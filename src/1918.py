def main():
    string = input()
    
    stack = []
    
    op_dict = dict()
    
    op_dict["*"] = 1
    op_dict["/"] = 1
    op_dict["+"] = 2
    op_dict["-"] = 2
    op_dict["("] = 3
    
    ans = ""
        
    for char in string:
        if char in op_dict:
            if char == "(":
                stack.append(char)
            elif len(stack) == 0:
                stack.append(char)
            else:
                while len(stack) != 0 and op_dict[stack[-1]] <= op_dict[char]:
                    ans += stack.pop()
                stack.append(char)
        else:
            if char == ")":
                while len(stack) != 0 and stack[-1] != "(" :
                    ans += stack.pop()
                stack.pop()
            else:
                ans += char
        
    while len(stack) != 0:
        ans += stack.pop()

    print(ans)
        
    
if __name__ == "__main__":
    main()