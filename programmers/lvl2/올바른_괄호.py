def solution(s):
    answer = True
    
    st = []
    
    for i in s:
        if i == "(":
            st.append(i)
        else:
            if not st or st.pop() != "(":
                return False
    
    return len(st) == 0