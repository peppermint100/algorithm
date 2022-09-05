size = 7
s1 = "1 1 2 3 4 2 1"

l = list(map(int, s1.split(" ")))

st = [0]
ans = [-1] * size

m = dict()

for i in range(size):
    c = l[i]

    if c in m.keys():
        m[c]+=1
    else:
        m[c] = 1

print(m)

for i in range(size):
    while st and m[l[st[-1]]] < m[l[i]]:
        ans[st.pop()] = l[i]
    st.append(i)

print(*ans)