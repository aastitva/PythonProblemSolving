def twoSum(nums, target):
    numMap = {}
    for i, num in enumerate(nums):
        if target - num in numMap:
            return [numMap[target - num], i]
        numMap[num] = i



def main():
    nums = [2, 7, 11, 15]
    #nums = [3, 2, 4]
    #nums = [3, 3]
    target = 9
    print(twoSum(nums, target))

if __name__ == '__main__':
    main()