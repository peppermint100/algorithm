# s1 = "A*(B+C)"
s1 = "ABC*+DE/-"


st = []
ans = []

for i in range(len(s1)):
    c = s1[i]

    if c.isalpha():
        ans.append(c)
    else:
        if c == "(":
            st.append(c)
        elif c == "*" or c == "/":
            while st and (st[-1] == "*" or st[-1] == "/"):
                ans.append(st.pop())
            st.append(c)
        elif c == "+" or c == "-":
            while st and st[-1] != "(":
                ans.append(st.pop())
            st.append(c)
        elif c == ")":
            while st and st[-1] != "(":
                ans.append(st.pop())
            st.pop()
    print("c = ", c)
    print("st = ", st)
    print("ans = ", ans)

while st:
    ans+=st.pop()


print("".join(ans))