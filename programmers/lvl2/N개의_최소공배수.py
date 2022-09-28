def solution(arr):
    arr.sort()
    
    answer = arr[0] 
    
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i]) 
        
    return answer

def gcm(a, b):
    while b > 0:
    	a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcm(a, b))