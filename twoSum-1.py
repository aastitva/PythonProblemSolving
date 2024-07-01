def twoSum(numbers, target):
    L = 0 
    R = len(numbers) - 1
    while L < R:
        num_sum = numbers[L] + numbers[R]
        if num_sum == target:
            return [L, R]
        elif num_sum < target:
            L += 1
        elif num_sum > target:
            R -= 1

numbers = [[2,7,11,15],[2,3,4],[0,0,3,4],[1,2,3,4,5],[1,1,1,1,1,1,1,1],[1,2,3,4,5]]
target = [9,6,0,9,2,9]
for i in range(len(numbers)):
    print(twoSum(numbers[i], target[i]))