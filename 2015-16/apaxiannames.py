#!/bin/python

community=raw_input()
n=input()
princess = 0
baron = 0
priest = 0
commoner = 0
for x in range(0, n):
	person=raw_input()
	if (person.startswith(community)):
		princess = princess + 1

	elif (person.endswith(community)):
		baron = baron + 1

	elif (person.find(community)!=-1):
		priest = priest + 1

	else:
		commoner = commoner + 1

print str(princess) + " PRINCESS"
print str(baron) + " BARON"
print str(priest) + " PRIEST"
print str(commoner) + " COMMONER"