def solution(n):
    a = [False,False] + [True]*(n-1)
    
    for i in range(2, n+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False
    
    total = 0
    
    for i in a:
        if i:
            total+=1
            
    return total 
