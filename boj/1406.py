import sys

text = list(sys.stdin.readline().strip(" "))
text.pop()
size = int(sys.stdin.readline())

cursor = len(text)

for i in range(size):
	command = sys.stdin.readline()
	
	if command.startswith("P"):
		text_to_add = list(command.strip(" "))
		text_to_add.pop()
		text = text[0:cursor] + [text_to_add[-1]] + text[cursor:]

		cursor+=1
	if command[0] == "L" and cursor > 0:
		cursor=cursor - 1
	if command[0] == "D" and cursor < len(text):
		cursor=cursor + 1
	if command[0] == "B" and cursor > 0:
		cursor-=1

print("".join(text))



		