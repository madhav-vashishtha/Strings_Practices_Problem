def reversePrefix(word, ch):
    if ch not in word:
        return word

    idx = word.index(ch)

    result = word[:idx+1][::-1] + word[idx+1:]
    return result


print(reversePrefix("abcdefd", "d"))  
print(reversePrefix("xyxzxe", "z"))  
print(reversePrefix("abcd", "z"))  

