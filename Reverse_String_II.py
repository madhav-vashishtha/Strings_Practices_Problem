def reverseStr(s, k):
    result = ""
    
    for i in range(0, len(s), 2 * k):
        result += s[i:i+k][::-1]
        result += s[i+k:i+2*k]
    
    return result

print(reverseStr("abcdefg", 2))

print(reverseStr("abcd", 2))


