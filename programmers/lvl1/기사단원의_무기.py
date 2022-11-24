# 최초 접근 => 시간초과로 실패
def solution(number, limit, power):
    answer = 0
    knights = []
    
    for i in range(1, number+1):
        knights.append(i)
    
    for x in knights:
        ap = get_attack_point(x)
        if ap > limit:
            answer+=power
        else:
            answer+=ap
    
    return answer

def get_attack_point(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count+=1
    return count
    
