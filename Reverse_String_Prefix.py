def reverseFirstK(s, k):
    first_part = s[:k]    
    rest_part = s[k:]    
    return first_part[::-1] + rest_part   

print(reverseFirstK("abcd", 2)) 
print(reverseFirstK("xyz", 3)) 
print(reverseFirstK("hey", 1)) 


