def detectCapitalUse(word):
    if word.isupper() or word.islower() or word.istitle():
        return True
    else:
        return False


print(detectCapitalUse("USA"))    
print(detectCapitalUse("leetcode"))
print(detectCapitalUse("Google"))
print(detectCapitalUse("FlaG")) 

