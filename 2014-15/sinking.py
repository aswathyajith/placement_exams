N, M, S, R = map(int, raw_input().split())

x_ship = []
y_ship = []
x_shot = []
y_shot = []
score = 0
mhtn = 0
sunk_ship = []

def manhattan(x1, x2, y1, y2):
	m = abs(x1-x2) + abs(y1-y2)
	return m

for i in range(0, S):
	x, y = map(int, raw_input().split())
	x_ship.append(x)
	y_ship.append(y)
	sunk_ship.append(0)

for i in range(0, R):
	x, y = map(int, raw_input().split())
	x_shot.append(x)
	y_shot.append(y)

sunk =0

for i in range(0, R):
	mhtn_list=[]
	for j in range(0, S):
		mhtn = manhattan(x_shot[i], x_ship[j], y_shot[i], y_ship[j])
		mhtn_list.append(mhtn)
	#print mhtn_list
	if (min(mhtn_list) == 0):
		sunk_ship[mhtn_list.index(0)] = 1
		score += 1000
		sunk += 1
	else:
		for j in range(0, S):
			if (sunk_ship[j] == 1):
				mhtn_list[j] = M*N
		score += max(0, 1000-min(mhtn_list) * 100)

print `sunk` + "/" + `S` + " ships sunk. Score: " + `score` + " points"