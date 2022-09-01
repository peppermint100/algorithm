import sys

s = open("10845input.txt", "rt") 

size = int(s.readline().strip())
q = []

for i in range(size):
    x = s.readline().strip().split()

    c = x[0]

    if c == ("push"):
        el = x[1]
        q.append(el)
    if c == "pop":
        if len(q) <= 0:
            print(-1)
        else:
            print(q.pop(0))
    elif c == "front":
        if len(q) <= 0:
            print(-1)
        else:
            print(q[0])
    elif c == "back":
        if len(q) <= 0:
                print(-1)
        else:
            print(q[len(q)-1])
    elif c == "size":
        print(len(q))
    elif c == "empty":
        if len(q) <= 0:
            print(1)
        else:
            print(0)
    