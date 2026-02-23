def maxRepeating(sequence, word):
    k = 0

    while word * (k + 1) in sequence:
        k += 1
        
    return k


print(maxRepeating("ababc", "ab")) 
print(maxRepeating("ababc", "ba")) 
print(maxRepeating("ababc", "ac")) 

