def countSubstrings(patterns, word):
    count = 0

    for p in patterns:
        if p in word:
            count += 1

    return count

print(countSubstrings(["a","abc","bc","d"], "abc"))
print(countSubstrings(["a","b","c"], "aaaaabbbbb"))
print(countSubstrings(["a","a","a"], "ab"))


