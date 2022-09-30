
answer = 0

def solution(numbers, target):
    global answer
    dfs(numbers, 0, 0, target)
    return answer 


def dfs(numbers, current_idx, result, target):
    global answer
    if current_idx == len(numbers):
        if result == target:
            answer+=1
        return
        
    dfs(numbers, current_idx+1, result+numbers[current_idx], target)
    dfs(numbers, current_idx+1, result-numbers[current_idx], target)
