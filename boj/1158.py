import sys

a = sys.stdin.readline()
b = a.split(" ")

size = int(b[0])
t = int(b[1]) - 1

l = []
r = []

for i in range(size):
    l.append(i+1)

start = 0
curr_size = len(l)

while curr_size > 0:
    pos = (start + t) % curr_size
    el = l[pos]
    r.append(el)
    l = l[:pos] + l[pos+1:]

    start = pos
    curr_size = len(l)

res = ", ".join(str(_) for _ in r)
print("<" + res + ">")