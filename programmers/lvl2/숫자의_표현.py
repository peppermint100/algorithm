def solution(n):
    answer = 0
    
    size = n // 2
    
    for i in range(1, size+1):
        total = 0
        curr = i
        
        while curr < n:
            total+=curr
            curr+=1
            if total > n:
                break
            if total == n:
                answer+=1
                break
        total = 0
        
    return answer+1
