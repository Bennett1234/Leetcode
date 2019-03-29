def lengthOfLastword(s):
    token = s.strip().split(' ')
    return(len(token[-1]))
