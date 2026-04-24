def furthestDistance(moves):
    L = moves.count('L')
    R = moves.count('R')
    underscore = moves.count('_')
    
    return abs(R - L) + underscore


print(furthestDistance("L_RL__R"))
print(furthestDistance("_R__LL_"))  
print(furthestDistance("_______")) 



