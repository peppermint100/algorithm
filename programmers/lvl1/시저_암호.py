def solution(s, n):
    answer = ''
    
    for i in s:
        pos = ord(i)
        _sum = pos + n
        if 65 <= pos <= 90:
            if _sum > 90:
                _sum-=26
            answer+=chr(_sum)
        elif 97 <= pos <= 122:
            if _sum > 122:
                _sum-=26
            answer+=chr(_sum)
        else:
            answer+=i
            
    return answer