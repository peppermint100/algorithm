
from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        curr = q.popleft()
        cnt = 0
        
        for i in q:
            if curr > i:
                cnt+=1
                break
            cnt+=1
        answer.append(cnt)

    return answer 
