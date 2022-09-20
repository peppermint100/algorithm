def solution(A,B):
    answer = 0
    
    size = len(A)
    A.sort()
    B.sort(reverse=True)
    
    for i in range(size):
        mx = A[i]
        mn = B[i]
        
        answer+=mx*mn
        
    return answer