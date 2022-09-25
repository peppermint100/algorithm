def solution_second_approach(s): 
    st = []
    l = list(s)
    
    for i in s:
        st.append(i)
        while len(st) > 1 and st[-1] == st[-2]:
                st.pop()
                st.pop()
    
    
    return 0 if st else 1 

def solution_brute_force_first_approach(s):
    ls = list(s)
    
    while ls:
        lls = len(ls)
        sls = shorten(ls)
        
        if len(sls) == lls:
            return 0
        else:
            ls = sls
            
    return 1 


def shorten(l):
    idx = 0
    
    while idx < len(l)-1:
        c = l[idx]
        n = l[idx+1]
        f_idx = idx
        idx+=1
        if c == n:
            f = l.pop(idx-1)
            s = l.pop(idx-1)
            idx = f_idx
    
    return l
    