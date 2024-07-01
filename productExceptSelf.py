def productExceptSelf(nums):
    mult = 1
    result = [0] * len(nums)
    zero_count = 0
    for num in nums:
        print(f"num: {num} mult: {mult}")
        if num == 0:
            mult *= 1
            zero_count += 1
            continue
        else:
            mult *= num
    print(f"mult: {mult}")
    for i in range(len(nums)):
        if nums[i] == 0 and zero_count == 1:
            result[i] = mult
        elif zero_count > 0 and nums[i] == 0:
            result[i] = 0
        elif zero_count > 0 and nums[i] != 0:
            result[i] = 0
        else:
            result[i] = mult // nums[i]
    return result

def productExceptSelf2(nums):
    result = [0] * len(nums)
    prefix = 1
    postfix = 1
    for i in range (len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result   

def main():
    nums = [[1,2,3,4],[0,0],[1,0],[-1,1,0,-3,3]]
    for num in nums:
        #print(productExceptSelf(num))
        print(productExceptSelf2(num))


if __name__ == '__main__':
    main()