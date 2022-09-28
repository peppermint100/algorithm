p_map = {
    "]": "[",
    ")": "(",
    "}": "{",
}

closer = list(p_map.keys())
opener = list(p_map.values())

def solution(s):
    answer = 0 
    
    if is_valid(s):
        answer+=1
    
    for i in range(1, len(s)):
        s = shift(s)
        if is_valid(s):
            answer+=1
    
    return answer

def shift(s):
    ns = ""
    
    for i in range(1, len(s)):
        ns+=s[i]
    
    return ns + s[0]

def is_valid(s):
    st = []
    for i in s:
        if not st and i in opener:
            st.append(i)
        elif not st and i in closer:
            return False
        elif i in opener:
            st.append(i)
        else: # st and closer
            if p_map[i] == st[-1]:
                st.pop()
            else:
                return False
            
    return True if not st else False