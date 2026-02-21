def isAcronym(words, s):
    acronym = ""
    for word in words:
        acronym += word[0]

    return acronym == s


print(isAcronym(["alice","bob","charlie"], "abc")) 
print(isAcronym(["an","apple"], "a"))               
print(isAcronym(["never","gonna","give","up","on","you"], "ngguoy")) 



