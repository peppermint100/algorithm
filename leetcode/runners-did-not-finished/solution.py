participant = ["iksu", "ingyu", "inan", "iksu"]
completion = ["iksu"]


d = {}
for x in participant:
    d[x] = d.get(x, 0) + 1

for x in completion:
    d[x]-=1

dnf = [k for k,v in d.items() if v > 0] # keys in dict, if v > 0 append to array

print(dnf)