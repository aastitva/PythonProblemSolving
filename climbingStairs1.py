def climbingStairs(nums):
    sum = 0
    num1 = 1
    num2 = 2
    if nums == 1:
        return 1
    if nums == 2:
        return 2
    while nums > 2:
        sum = num1 + num2
        num1 = num2
        num2 = sum
        nums -= 1
    return sum

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,44]
for i in num:
    #pass
    print(f"{i} : {climbingStairs(i)}")