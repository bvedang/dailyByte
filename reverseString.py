s = "CAt"

def reverseString(s)->str:
    """Takes String as Argument and return's reverse of the given string"""
    res=""
    for i in range(len(s)-1,-1,-1):
        res += s[i]

    return res

print(reverseString(s))