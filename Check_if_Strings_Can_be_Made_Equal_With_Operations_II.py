def checkStrings(s1, s2):

    even1 = sorted(s1[0::2])
    even2 = sorted(s2[0::2])

    odd1 = sorted(s1[1::2])
    odd2 = sorted(s2[1::2])

    if even1 == even2 and odd1 == odd2:
        return True
    else:
        return False
    
s1 = "abcdba"
s2 = "cabdab"

print(checkStrings(s1, s2))

s1 = "abe"
s2 = "bea"

print(checkStrings(s1, s2))


