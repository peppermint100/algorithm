import sys

size = int(sys.stdin.readline())

for i in range(size):
    p = list(str(sys.stdin.readline()).strip(" "))
    sum = 0
    text_size = len(p)
    
    for j in range(text_size):
        if p[j] == "(":
            sum += 1
        elif p[j] == ")":
            sum -= 1
        
        if sum < 0:
            print("NO")
            break
    
    if sum > 0:
        print("NO")

    if sum == 0:
        print("YES")
    
