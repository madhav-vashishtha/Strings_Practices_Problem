def longestCommonPrefix(arr1, arr2):
    ans = 0

    for x in arr1:
        for y in arr2:
            s1 = str(x)
            s2 = str(y)

            count = 0

            for i in range(min(len(s1), len(s2))):
                if s1[i] == s2[i]:
                    count += 1
                else:
                    break

            ans = max(ans, count)

    return ans


arr1 = [1, 10, 100]
arr2 = [1000]

print(longestCommonPrefix(arr1, arr2))  


arr1 = [1, 2, 3]
arr2 = [4, 4, 4]

print(longestCommonPrefix(arr1, arr2))   


