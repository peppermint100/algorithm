# 다시 뒤에 추가시켜도 순서는 유지된다.
def solution(priorities, location):
    answer = 0
    
    while 1:
        curr_m = max(priorities)
        
        for i in range(len(priorities)):
            if priorities[i] == curr_m:
                answer+=1
                priorities[i] = 0
                curr_m = max(priorities)
                
                if location == i:
                    return answer
    
    return answer