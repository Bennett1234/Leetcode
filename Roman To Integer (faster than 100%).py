def romanToNum(x):
    l = len(x)
    i = 0
    dic_ = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    s = 0
    while i < l:
        if i < l-1 and ((x[i] == 'I' and x[i+1] in ('V','X')) or \
        (x[i] == 'X' and x[i+1] in ('L','C')) or \
        (x[i] == 'C' and x[i+1] in('D','M'))):
            s += dic_[x[i+1]]-dic_[x[i]]
            i += 2
        else:
            s += dic_[x[i]]
            i += 1
    return s
