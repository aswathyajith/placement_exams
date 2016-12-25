def mccarthy(n):
	if (n > 100):
		return n-10
	else:
		return mccarthy(mccarthy(n+11))

n = input()
print mccarthy(n)