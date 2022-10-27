
from itertools import permutations

def solution(numbers):
    answer = 0
    l = []

    for i in range(1, len(numbers)+1):
        a = list(permutations(list(numbers), i))
        for j in a:
            target = ""
            for k in j:
                target+=str(k)
            l.append(int(target))

    for i in set(l):
        if is_prime(i):
            answer+=1

    return answer

def is_prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True
