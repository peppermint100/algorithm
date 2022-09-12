def solution(n, arr1, arr2):
    answer = []
    
    bin1 = list(map(toBin, arr1, [n] * n))
    bin2 = list(map(toBin, arr2, [n] * n))
    
    for i in range(n):
        curr = ""
        
        pos1 = bin1[i]
        pos2 = bin2[i]
        
        for j in range(n):
            if pos1[j] == "1" or pos2[j] == "1":
                curr+="#"
            else:
                curr+=" "
        answer.append(curr)
        
    return answer

def toBin(n, total_size):
    res = bin(n)[2:]
    size = len(res)
    
    while len(res) < total_size:
        res = "0" + res
            
    return res
        
