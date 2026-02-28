def minimizedStringLength(s):
    unique_chars = set(s)
    
    return len(unique_chars)


# Example tests
print(minimizedStringLength("aaabc"))  
print(minimizedStringLength("cbbd"))   
print(minimizedStringLength("baadccab"))

