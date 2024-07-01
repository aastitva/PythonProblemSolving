def bubbleSort(nums):

    for i in range(len(nums)):
        flag = 0
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                flag = 1
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if flag == 0:
            return nums
    return nums

nums = [[64, 34, 25, 12, 22, 11, 90], [12, 11, 13, 5, 6], [5, 3, 2, 4, 1], [1, 2, 3, 4, 5], [1], [1, 2], [2, 1], [1, 2, 3], [3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 3, 2, 4], [1, 3, 2, 4, 5], [1, 3, 2, 4, 5, 6], [1, 3, 2, 4, 5, 6, 7], [1, 3, 2, 4, 5, 6, 7, 8], [1, 3, 2, 4, 5, 6, 7, 8, 9], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [-2, 45, 0,]]
for i in range(len(nums)):
    print(bubbleSort(nums[i]))