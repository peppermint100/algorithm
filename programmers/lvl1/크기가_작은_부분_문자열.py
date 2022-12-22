
def solution(t, p):
    answer = 0
    
    size = len(t) - len(p)
    
    for i in range(0, size+1):
        curr = t[i:len(p) + i]
        if int(p) >= int(curr):
            answer+=1
    return answer
