def DFS(v):
	visited[v]=1
	for x in graph[v]:
		if (visited[x] != 1):
			DFS(x)

	return

graph={}
visited={}
v=input()
e=input()
for x in range(0,v):
	graph[x]=[]
	visited[x]=0
for x in range(0,e):
	start, end=map(int,raw_input().split())
	graph[start].append(end)
	graph[end].append(start)

DFS(0)
count = 1
for x in range(0,v):
	if (visited[x] == 0):
		count = count + 1
		DFS(x)
print count