def gcd(a, b):
	if (a == b):
		return a
	elif (a > b):
		return gcd(a-b,b)
	else:
		return gcd(a,b-a)

a,b = map(int, raw_input().split())
print gcd(a,b)
