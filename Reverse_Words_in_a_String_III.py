def reverse_words(s):
    words = s.split(" ")       
    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])  

    return " ".join(reversed_words)


s1 = "Let's take LeetCode contest"
print(reverse_words(s1))  

s2 = "Mr Ding"
print(reverse_words(s2)) 



