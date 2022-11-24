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
    

# 약수 구하는 함수 최적화.. 그래도 실패
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
    if n == 1:
        return 1
    count = 2
    
    for i in range(2, n // 2+1):
        if n % i == 0:
            count+=1
    return count

# a*b = c 에서 a,b가 c의 약수임을 이용
# 최초 1로 가득찬 배열(1은 모두의 약수이므로) 선언하고 1부터 순회하며 약수를 1개씩 더해줌
def solution(number, limit, power):
    answer = 0
    
    weapons = [0] + [1] * number
    
    for i in range(1, number+1):
        j = 2
        while i * j <= number:
            weapons[i*j]+=1
            j+=1
            
    for w in weapons:
        if w > limit:
            answer+=power
        else:
            answer+=w
    
    return answer
