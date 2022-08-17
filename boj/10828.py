import sys

size = int(sys.stdin.readline())

stack = [] 

for i in range(1, size+1):
    t = sys.stdin.readline().split()
    command = t[0]
    
    if command.startswith("push"):
        v = t[1]
        stack.append(v)
    
    elif command == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    
    elif command == "size":
        print(len(stack))

    elif command == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command == "empty":
        if (len(stack)) > 0:
            print(0)
        else:
            print(1)

