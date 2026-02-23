def second_largest_digit(s):
    digits = set()  
  
    for ch in s:
        if ch.isdigit():
            digits.add(int(ch))
    
    digits = sorted(digits, reverse=True) 
    
    if len(digits) < 2:
        return -1
    else:
        return digits[1]


print(second_largest_digit("dfa12321afd"))
print(second_largest_digit("abc1111"))   

