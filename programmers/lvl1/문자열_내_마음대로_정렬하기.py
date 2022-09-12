def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])


# strings[n]을 각 strings의 원소에 맨 앞에 붙여준 다음 sort를 하는 풀이법도 있음