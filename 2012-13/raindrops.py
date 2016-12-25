n = input()
temp_list = map(int, raw_input().split())
sum = 0
count =0
for x in temp_list:
	if (x >= 0):
		count += 1
		sum += x

if count==0:
	print "INSUFFICIENT DATA"
else:
	print sum/count