def swap_even(name, end):
    trans_name=''
    for i in range(0, end, 2):
        trans_name = trans_name + name[i+1]
        trans_name = trans_name + name[i]
    return trans_name 

name = raw_input()
n = len(name)
if (n%2 == 0): 
    print swap_even(name, n-1)
else:
    print swap_even(name, n-2) + name[-1]
