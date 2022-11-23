def solution(babbling):
    answer = 0
    w_list = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        stack = ""
        prev = ""
        
        for c in word:
            stack+=c
            
            if stack != prev and (stack in w_list):
                prev = stack
                stack = ""
            
        if len(stack) == 0:
            answer+=1
        
    return answer



