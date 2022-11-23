# 단순한 풀이 시간 복잡도 O(N*M)
def solution(numbers):
    answer = 0 
    
    sn = sorted(numbers)
    m = [0,1,2,3,4,5,6,7,8,9]
    
    for x in m:
        if x not in sn:
            answer+=x
        
    return answer


# 0~9 총합이 45이므로 있는 값들을 제외하는 방식 O(N)
def solution(numbers):
    answer = 45
    for i in range(len(numbers)):
        answer -= numbers[i]
    return answer

def solution(numbers):
    return 45 - sum(numbers)

