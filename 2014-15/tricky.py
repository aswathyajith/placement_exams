def value(ch):
	value = 0
	if (ch == '1'):
		value = 1
	elif (ch == '2'):
		value = 2
	elif (ch == '3'):
		value = 3
	elif (ch == '4'):
		value = 4
	elif (ch == '5'):
		value = 5
	elif (ch == '6'):
		value = 6
	elif (ch == '7'):
		value = 7
	elif (ch == '8'):
		value = 8
	elif (ch == '9'):
		value = 9
	elif (ch == 'J'):
		value = 10
	elif (ch == 'Q'):
		value = 11
	elif (ch == 'K'):
		value = 12
	elif (ch == 'A'):
		value = 13

	return value

n = input()
list_1 = raw_input().split()
list_2 = raw_input().split()
player1 = 0
player2 = 0

for i in range(0,n):
	if (value(list_1[i]) > value(list_2[i])):
		player1 += 1
	elif (value(list_1[i]) < value(list_2[i])):
		player2 += 1

if player1 > player2:
	print "PLAYER 1 WINS"

elif player2 > player1:
	print "PLAYER 2 WINS"

else:
	print "TIE"
