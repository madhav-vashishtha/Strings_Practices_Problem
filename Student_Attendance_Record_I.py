def checkRecord(s):
    if s.count('A') >= 2:
        return False
    
    if "LLL" in s:
        return False
    
    return True

print(checkRecord("PPALLP"))  
print(checkRecord("PPALLL"))

