# by recursion
def climbstairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = [1,2]
    for i in range(3,n+1):
        result.append(result[-1]+result[-2])
    return result[-1]
