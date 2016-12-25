def square(x, n):
    if (n == 0):
        return 1
    elif (n==1):
        return x
    elif (n > 0 and ((n % 2) == 0)):
        return square(x*x, n/2)
    elif (n > 0 and ((n % 2) == 1)):
        return x*square(x*x, (n-1)/2)

x, n = map(int, raw_input().split())
print square(x, n)
