class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        
        setA = set()
        setB = set()
        result = []
        
        for i in range(n):
            setA.add(A[i])
            setB.add(B[i])
            
            count = 0
            
            for num in setA:
                if num in setB:
                    count += 1
            
            result.append(count)
        
        return result
    
A = [1,3,2,4]
B = [3,1,2,4]

obj = Solution()
print(obj.findThePrefixCommonArray(A, B))

A = [2,3,1]
B = [3,1,2]

obj = Solution()
print(obj.findThePrefixCommonArray(A, B))


