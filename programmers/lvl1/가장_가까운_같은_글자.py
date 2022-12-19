def solution(s):
    answer = []
    
    dic = dict()
    
    for i in range(len(s)):
        curr = s[i]
        
        if curr not in dic:
            answer.append(-1)
        else:
            diff = i - dic[curr]
            answer.append(diff)
            
        dic[curr] = i 
        
    return answer
