def climbingStairsRecursive(num, memo):
    if num <= 1:
        return num
    if num in memo:
        return memo[num]
    memo[num] = climbingStairsRecursive(num-1, memo) + climbingStairsRecursive(num-2, memo)
    return memo[num]

memo = {}
print(climbingStairsRecursive(3, memo))

