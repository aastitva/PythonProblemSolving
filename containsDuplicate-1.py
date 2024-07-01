def containsNearbyDuplicate(nums, k):

    hashSet = set()    
    L = 0

    for R in range(len(nums)):
        if R > L + k:
            hashSet.remove(nums[L])
            L += 1
        if nums[R] in hashSet:
            return True
        hashSet.add(nums[R])
    return False

nums = [[1,2,3,1],[1,0,1,1],[1,2,3,1,2,3],[1,2,2,1],[99,99]]
k = [3,1,2,2,2]
for i in range(len(nums)):
    print(containsNearbyDuplicate(nums[i], k[i]))
#print(containsNearbyDuplicate(nums, k))
