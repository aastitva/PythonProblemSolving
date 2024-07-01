def maxProduct(nums):
    curr_max = 1
    curr_min = 1
    overall_max = float('-inf')
    for num in nums:
        temp = curr_max
        curr_max = max(num, num * curr_max, num * curr_min)
        curr_min = min(num, num * temp, num * curr_min)
        overall_max = max(overall_max, curr_max)
    return overall_max

def maxProduct2(nums):
    prod = 1
    max_prod = float('-inf')
    for num in nums:
        prod *= num
        max_prod = max(max_prod, prod)
        if prod == 0:
            prod = 1
    return max_prod

def maxProduct3(nums):
    left_prod, right_prod, max_prod = 1, 1, nums[0]
    for i in range(len(nums)):
        left_prod *= nums[i]
        right_prod *= nums[-i-1]
        max_prod = max(max_prod, left_prod, right_prod)
        if left_prod == 0:
            left_prod = 1
        if right_prod == 0:
            right_prod = 1
    return max_prod

def maxProduct4(nums):
    cur_max = 1
    cur_min = 1
    max_prod = nums[0]
    for n in nums:
        if n == 0:
            cur_max, cur_min = 1, 1
            max_prod = max(max_prod, 0)
            continue
        tmp = cur_max * n
        cur_max = max(n*cur_max, n*cur_min, n)  
        cur_min = min(tmp, n*cur_min, n)
        max_prod = max(max_prod, cur_max)
    return max_prod

inputs = [[2,3,-2,4], [-2,0,-1], [3,-1,4], [2,-5,-2,-4,3], [0,2], [-2,1,-3,4,-1,2,1,-5,4]]
for input in inputs:
    #print(maxProduct(input))
    #print(maxProduct2(input))
    print(maxProduct3(input))
    print(maxProduct4(input))
