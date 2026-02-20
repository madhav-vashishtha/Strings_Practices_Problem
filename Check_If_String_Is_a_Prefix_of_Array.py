def isPrefixString(s, words):
    result = ""

    for word in words:
       result += word

       if result == s:
            return True
       
       if len(result) > len(s):
           return False
       
    return False

print(isPrefixString("iloveleetcode", ["i","love","leetcode","apples"]))

print(isPrefixString("iloveleetcode", ["apples","i","love","leetcode"]))

