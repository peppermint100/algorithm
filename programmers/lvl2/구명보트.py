# python pop은 효율이 좋지 않다.
# 투포인터 이용
def solution(people, limit):
    boat = 0
    
    sorted_caramel = sorted(people)
    
    l = 0
    r = len(people)-1
    
    while l < r:
        if limit >= sorted_caramel[l] + sorted_caramel[r]:
            l+=1
            r-=1
            boat+=1
        else:
            r-=1
            boat+=1
            
    if l == r:
        boat+=1
            
    return boat