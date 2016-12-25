n = input()
temps = map(int, raw_input().split())
count = 0

for temp in temps:
	if (temp < 0):
		count += 1

print count