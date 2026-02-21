def restoreString(s, indices):
    result = [""] * len(s)
    
    for i in range(len(s)):
        result[indices[i]] = s[i]

    return "".join(result)


print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))  
print(restoreString("abc", [0,1,2])) 
