# first convert to character then combine together and conver to int and finally separate them again
def plusOne(s):
    l = int(''.join(list(map(str,s))))+1
    return([int(t) for t in str(l)])
