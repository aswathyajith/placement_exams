name = raw_input()
n=len(name)
new_name=''
for x in range(0,n):
	if(new_name == ''):
		new_name = name[x]
	elif (new_name[-1] == name[x]):
		new_name = new_name 
	else:
		new_name = new_name + name[x] 
print new_name