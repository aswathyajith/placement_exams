

def check(x_list, y_list):
    flag = 0
    for i in range(0, N):
        x,y =  x_list[i], y_list[i]
        if (x_list.count(x) > 1 or y_list.count(y) > 1):
            flag = 1
        for j in range(0,N):
            x2,y2 = x_list[j],y_list[j]
            if (i != j and abs(x-x2) == abs(y-y2)):
                flag = 1

    return flag

N = input()
x_list = []
y_list = []
for i in range(0, N):
    x, y = map(int, raw_input().split())
    x_list.append(x)
    y_list.append(y)
if check(x_list, y_list)==1:
    print "INCORRECT"
else:
    print "CORRECT"
