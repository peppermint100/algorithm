
def solution(arr):
    st = [-1]

    for i in arr:
        if st[-1] == i:
            continue
        st.append(i)

    return st[1:]
