# s1 = "()(((()())(())()))(())"
s1 = "(((()(()()))(())()))(()())"

size = len(s1)

count = 0
total = 0

for i in range(size):
    c = s1[i]

    # is razor
    if i+1 < size and c == "(" and s1[i+1] == ")":
        total+=count
        continue

    if i-1 >= 0 and s1[i-1] == "(" and c == ")":
        continue

    if c == "(":
        count+=1

    if c == ")":
        total+=1
        count-=1

print(total)

        