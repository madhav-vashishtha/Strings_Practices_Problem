def getCommon(nums1, nums2):
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] == nums2[j]:
            return nums1[i]
        
        elif nums1[i] < nums2[j]:
            i += 1

        else:
                j += 1

    return -1

nums1 = [1,2,3]
nums2 = [2,4]

print(getCommon(nums1, nums2))

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]

print(getCommon(nums1, nums2))


