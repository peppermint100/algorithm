size = 4
s1 = "3 5 2 7"

l = list(map(int, s1.split(" ")))

st = [0]
ans = [-1] * size

for i in range(size):
    while st:
        if l[i] > l[st[-1]]:
            ans[st.pop()] = l[i]
        else:
            st.append(i)
            break

    print("st = ", st)
    
    if not st:
        st.append(i)

print(*ans)

        