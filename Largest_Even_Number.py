def largestEvenNumber(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '2':
            return s[:i+1]  
    
    return ""   

print(largestEvenNumber("1112"))
print(largestEvenNumber("221"))
print(largestEvenNumber("1"))
