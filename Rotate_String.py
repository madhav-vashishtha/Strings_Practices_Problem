def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    
    if goal in (s + s):
        return True
    
    return False


print(rotateString("abcde", "cdeab"))  
print(rotateString("abcde", "abced"))  


