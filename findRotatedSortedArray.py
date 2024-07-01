def findInRotatedSortedArray(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

nums = [4,5,6,7,0,1,2]
print(findInRotatedSortedArray(nums, 0))
nums = [9,12,15,17,25,28,32,37,3,4,5,6,7]
print(findInRotatedSortedArray(nums, 3))
print(findInRotatedSortedArray(nums, 0))
nums = [1]
print(findInRotatedSortedArray(nums, 1))
nums = [1,3]
print(findInRotatedSortedArray(nums, 3))
nums = [1,3,5]
print(findInRotatedSortedArray(nums, 5))