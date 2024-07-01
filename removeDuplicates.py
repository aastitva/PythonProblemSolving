
def removeDuplicates(nums):
    L = 0
    expectedNums = {}
    for num in nums:
        print(f"num: {num}, expectedNums: {expectedNums}")
        if num not in expectedNums:
            expectedNums[num] = 1 + expectedNums.get(num, 0)
        
    for n in expectedNums:
        nums[L] = n
        L += 1
    return len(nums), nums

nums = [[1,1,2],[0,0,1,1,1,2,2,3,3,4]]
for i in range(len(nums)):
    print(f"nums: {nums[i]} {removeDuplicates(nums[i])}")