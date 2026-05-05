def rotateRight(nums, k):
    n = len(nums)
    
    if n == 0:
        return nums
    
    k = k % n   
    
    return nums[-k:] + nums[:-k]


nums1 = [1,2,3,4,5]
print(rotateRight(nums1, 2))  

nums2 = [0,1,2]
print(rotateRight(nums2, 4))  