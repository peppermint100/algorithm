
def solution(clothes):
    answer = 1

    dic = dict()

    for item in clothes:
        name, wear = item

        if wear in dic.keys():
            dic[wear].append(name)
        else:
            dic[wear] = [name]

    for v in dic.values():
        print(v)
        size = len(v) + 1
        answer *= size

    return answer - 1
