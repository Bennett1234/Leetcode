def reverse(x):
    y = str()
    if x > 0:
        x = str(x)
        y = x[::-1]
        y = int(y)
    else:
        x = str(-x)
        y = x[::-1]
        y =-1* int(y)
    if y < -2**31 or y > 2**31-1:
        y = 0
    return y
