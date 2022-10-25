
def solution(number, k):
    answer = ""
    
    st = []
    
    for num in number:
        if not st:
            st.append(num)
        else:
            while st and st[-1] < num and k > 0:
                k-=1
                st.pop()
            st.append(num)
    
    return "".join(st) 
