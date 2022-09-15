def solution(n):
    answer = []
    
    if n < 3:
        return n
    
    while 1:
        r = n % 3
        n = n // 3  
        answer.append(r)
        
        if n == 1 or n == 2:
            answer.append(n)
            break
        
    total = 0
    
    rvs = list(reversed(answer))
    
    for i in range(len(rvs)):
        total+=(3**i)*rvs[i]
        
    return total
