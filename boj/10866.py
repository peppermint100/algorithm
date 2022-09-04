import sys

s = open("10866_input.txt", "r")

size = int(s.readline().strip())

dq = []

for i in range(size):
    c = s.readline().strip().split("_")

    dq_empty = len(dq) == 0
    
    if c[0] == "push":
        d = c[1].split(" ")
        direction = d[0]
        val = d[1]

        if direction == "front":
            dq.insert(0, val)
        else:
            dq.append(val)

    if c[0] == "pop":
        if c[1] == "front":
            if dq_empty:
                print(-1)
            else:
                print(dq.pop(0))
        else:
            if dq_empty:
                print(-1)
            else:
                print(dq.pop())


    if c[0] == "size":
        print(len(dq))
    
    if c[0] == "empty":
        if dq_empty:
            print(1)
        else:
            print(0)

    if c[0] == "front":
        if dq_empty:
            print(-1)
        else:
            print(dq[0])
    
    if c[0] == "back":
        if dq_empty:
            print(-1)
        else:
            print(dq[-1])
    


        

        