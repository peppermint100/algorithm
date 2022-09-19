def solution(s):
    if s == '1':
        return [0, 0]
    
    c = s 
    z = 0
    count=0
    
    while c != '1':
        c, nz = convert(c)
        z+=nz
        count+=1
        
    return [count, z]

def convert(s):
    res = ''
    lost_zero = 0
    
    for i in s:
        if i=='1':
            res+='1'
        else:
            lost_zero+=1
    
    rl = len(res)
    return (bin(rl)[2:], lost_zero)
    