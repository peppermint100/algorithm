def solution(s):
    answer = ''
    
    s_list = s.split(" ")
    
    for i in s_list:
        if i == "":
            answer+=" "
        else:
            i = i.lower()
            
            if i[0].isalpha():
                answer+=i[0].upper() + i[1:]
            else:
                answer+=i
            answer+=" "
            
    return answer[:-1]