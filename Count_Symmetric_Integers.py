def countSymmetricIntegers(low, high):
    count = 0
    
    for num in range(low, high + 1):
        s = str(num)

        if len(s) % 2 != 0:
            continue
        
        mid = len(s) // 2
        
        first_half = s[:mid]
        second_half = s[mid:]

        sum1 = sum(int(d) for d in first_half)
        sum2 = sum(int(d) for d in second_half)
        
        if sum1 == sum2:
            count += 1
            
    return count

print(countSymmetricIntegers(1, 100))     
print(countSymmetricIntegers(1200, 1230))  

