def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        a = numbers[i]
        for j in range(len(numbers)):
            if i == j:
                continue
            b = numbers[j]
            answer.append(a+b)
            
    return sorted(set(answer))
