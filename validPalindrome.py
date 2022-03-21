s = "A man, a plan, a canal: Panama."
s = s.lower()

def validPalindrome(s):
    left = 0
    right = len(s)-1
    while(left<=right):
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(validPalindrome(s))