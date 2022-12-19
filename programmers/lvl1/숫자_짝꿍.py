
def solution(X, Y):
    answer = []
    
    x_dic = dict()
    y_dic = dict()
    for i in range(0, 10):
        x_dic[i] = 0
        y_dic[i] = 0
        
    for x in X:
        x_dic[int(x)]+=1
    for y in Y:
        y_dic[int(y)]+=1
    
    for i in range(9, -1, -1):
        while x_dic[i] > 0 and y_dic[i] > 0:
            x_dic[i]-=1
            y_dic[i]-=1
            answer.append(i)

    if answer and sum(answer) == 0:
    	return "0"
    if not answer:
    	return "-1"
    
    return ''.join(map(str, sorted(answer, reverse=True)))
