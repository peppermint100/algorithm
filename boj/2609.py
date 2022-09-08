def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

s1 = "24 18"

a, b = map(int, s1.split(" "))

bigger = max(a, b)
smaller = min(a, b)

g = gcd(bigger, smaller)

print(g)
print(int(a*b/g))


