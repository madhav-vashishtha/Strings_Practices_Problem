def robotSim(commands, obstacles):
    obstacle_set = set(map(tuple, obstacles))
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    x, y = 0, 0  
    d = 0         
    max_distance = 0
    
    for cmd in commands:
        if cmd == -1:
            d = (d + 1) % 4
        elif cmd == -2: 
            d = (d - 1) % 4
        else:
            for _ in range(cmd):
                nx = x + directions[d][0]
                ny = y + directions[d][1]
                
                if (nx, ny) in obstacle_set:
                    break
                
                x, y = nx, ny
                
                max_distance = max(max_distance, x*x + y*y)
    
    return max_distance

commands = [4, -1, 3]
obstacles = []

print(robotSim(commands, obstacles))

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]

print(robotSim(commands, obstacles))

commands = [6,-1,-1,6]
obstacles = [[0,0]]

print(robotSim(commands, obstacles))


