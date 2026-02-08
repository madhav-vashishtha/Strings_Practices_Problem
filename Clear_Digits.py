def removeDigits(s):
    s = list(s)  
    i = 0

    while i < len(s):
        if s[i].isdigit():
            j = i - 1

            while j >= 0 and s[j].isdigit():
                j -= 1

            if j >= 0:
                del s[i]   
                del s[j]  
                i = 0    
            else:
                i += 1
        else:
            i += 1

    return "".join(s)

print(removeDigits("abc"))  
print(removeDigits("cb34")) 
print(removeDigits("a1b2c3")) 


