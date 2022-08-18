import sys

size = int(sys.stdin.readline())

st = []
count = 1
res = True
res_list = []

for i in range(size):
	curr = int(sys.stdin.readline())

	while count <= curr:
		res_list.append("+")
		st.append(count)
		count+=1
	
	if st[-1] == curr:
		st.pop()
		res_list.append("-")
	else:
		res = False

if not res:
	print("NO")
else:
	print("\n".join(res_list))
	