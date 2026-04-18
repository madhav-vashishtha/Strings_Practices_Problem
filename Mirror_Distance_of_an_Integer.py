def mirror_distance(n):
    reversed_n = int(str(n)[::-1])
    
    return abs(n - reversed_n)

print(mirror_distance(25)) 
print(mirror_distance(10))
print(mirror_distance(7)) 


