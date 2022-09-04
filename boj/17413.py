
# s1 = "baekjoon online judge"
# s1 = "<open>tag<close>"
# s1 = "<ab cd>ef gh<ij kl>"
# s1 = "one1 two2 three3 4fourr 5five 6six"
s1 = "<int><max>2147483647<long long><max>9223372036854775807"
# s1  = "<   space   >space space space<    spa   c e>"

st = []
result = []

is_bracket = False

for i in range(len(s1)):
    c = s1[i]

    if c != "<" and c != ">":
        st.append(c)

    if c == "<":
        generated = "".join(reversed(st))
        result.append(generated)
        st = []

        is_bracket = True

    if c == ">":
        generated = "".join(["<"] + st + [">"])
        result.append(generated)
        st = []

        is_bracket = False


    if c == " " and is_bracket is False:
        st.pop()
        st.insert(0, " ")
        result.append("".join(reversed(st)))
        st = []


rest = ""
for i in reversed(range(len(st))):
    rest+=st[i]

answer = "".join(result + [rest])

# ?!
print(answer.replace("\n", ""))
