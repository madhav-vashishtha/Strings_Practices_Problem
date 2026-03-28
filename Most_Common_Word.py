def mostCommonWord(paragraph, banned):
    paragraph = paragraph.lower()
    
    for ch in "!?',;.":
        paragraph = paragraph.replace(ch, " ")
    
    words = paragraph.split()
    
    banned_set = set(banned)
    
    count = {}
    for word in words:
        if word not in banned_set:
            count[word] = count.get(word, 0) + 1
    
    max_word = ""
    max_count = 0
    
    for word in count:
        if count[word] > max_count:
            max_count = count[word]
            max_word = word
    
    return max_word

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph, banned))

paragraph = "a."
banned = []

print(mostCommonWord(paragraph, banned))

