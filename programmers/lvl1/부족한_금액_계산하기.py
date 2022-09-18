def solution(price, money, count):
    total = 0
    curr = 0
    
    for i in range(count):
        curr+=price
        total+=curr
        
    return total-money if total-money > 0 else 0