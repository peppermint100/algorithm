# f = open("2309_input.txt", "rt")

# l = []

# for i in range(9):
# 	l.append(int(f.readline().strip()))

l= [1,9,2,8,3,7,4,6,70]

a = sum(l)

ans = []

flag = False

for i in range(9):
	for j in range(i+1, 9):
		if a - l[i] - l[j] == 100:
			flag = True
			for k in range(9):
				if k == i or k ==j:
					continue
				ans.append(l[k])
		if flag:
			break
	if flag:
		break

for i in range(len(ans)):
	print(sorted(ans)[i])