
def merge_sorted(arr1, arr2, nums):
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            nums[k] = arr1[i]
            i += 1
        else:
            nums[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        nums[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        nums[k] = arr2[j]
        j += 1
        k += 1

    return nums

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge_sorted(left, right, nums)

nums = [[38,27,43,3,9,82,10],[38,27,43,3,9,82,10,1],[38,27,43,3,9,82,10,1,2],[38,27,43,3,9,82,10,1,2,4],[-100,100,0],[0,0,0,0],[0,1,1],[0,1,1,0],[0,1,1,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0,0],[18]]   
for num in nums:
    print(merge_sort(num))

    