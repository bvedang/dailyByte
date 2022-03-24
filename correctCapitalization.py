s="coding"

def vaildCapitalization(s):
    if s.islower():
        return True
    elif s.isupper():
        return True
    else:
        firstCapital = False
        middleCapital = False
        for i in range(len(s)):
            if i == 0 and s[i].isupper():
                firstCapital = True
            if i != 0 and s[i].isupper():
                middleCapital = True
        if firstCapital and not middleCapital:
            return True
        else:
            return firstCapital and middleCapital
        

print(vaildCapitalization(s))