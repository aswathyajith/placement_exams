def neighbor(matrix, i , j):
	# res=0
	# if (i==0):
	#  	if (j==0):
	# 		res = matrix[i+1][j+1] + matrix[i+1][j] + matrix[i][j+1]
	# 	elif (j==m-1):
	# 		res = matrix[i][j-1] + matrix[i+1][j-1] + matrix[i+1][j]

	# 	else:
	# 		res = matrix[i][j-1] + matrix[i][j+1] + matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]

	# elif (j==0):
	# 	if (i==n-1):
	# 		res = matrix[i-1][j]+ matrix[i-1][j+1] + matrix[i][j+1]
	# 	else:
	# 		res = matrix[i-1][j] + matrix[i-1][j+1] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j]

	# elif (i==n-1): 
	# 	if (j==m-1):
	# 		res = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i][j-1]
				
	# 	else:
	# 		res = matrix[i][j-1] + matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + matrix[i][j+1]
		
	# elif (j==m-1):
	# 	res = matrix[i-1][j] + matrix[i+1][j] + matrix[i-1][j-1] + matrix[i][j-1] + matrix[i+1][j-1]

	# if (i!=0 and j!=0 and i!=n-1 and j!=m-1):
	res = matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i][j+1] + matrix[i-1][j+1] + matrix[i-1][j] + matrix[i-1][j-1] + matrix[i][j-1]

	return res

n, m = map(int, raw_input().split())
matrix=[]
first_row = [0]*(m+2)
matrix.append(first_row)
for i in range(n):
	l=[0]
	col = map(int, raw_input().split())
	col.append(0)
	l.extend(col)
	matrix.append(col) 

second_row = [0]*(m+2)
matrix.append(second_row)

for i in range(1,n+1):
	out=''
	for j in range(m):
		if (matrix[i][j] == 1):
			out=out+'X'
		elif (neighbor(matrix, i , j) == 0):
			out=out+'-'
		else:
			out=out+`neighbor(matrix, i, j)`
	print out