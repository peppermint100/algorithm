import sys

size = int(sys.stdin.readline())

for i in range(size):
    text = sys.stdin.readline()
    split_text = text.split()

    reversed_text = []

    for word in split_text:
        reversed_text.append(word[::-1])
        reversed_text.append(" ")
    
    print("".join(reversed_text))