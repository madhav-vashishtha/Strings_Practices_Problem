def canReach(arr, start):
    visited = [False] * len(arr)

    def dfs(i):
        if i < 0 or i >= len(arr) or visited[i]:
            return False

        if arr[i] == 0:
            return True

        visited[i] = True

        return dfs(i + arr[i]) or dfs(i - arr[i])

    return dfs(start)


arr = [4,2,3,0,3,1,2]
start = 5
print(canReach(arr, start))  

arr = [4,2,3,0,3,1,2]
start = 0
print(canReach(arr, start))  

arr = [3,0,2,1,2]
start = 2
print(canReach(arr, start))   


