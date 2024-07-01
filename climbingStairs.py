def climbingStairs(num):
    if num == 1:
        return 1
    first = 1
    second = 2
    for i in range(3, num+1):
        third = first + second
        first = second
        second = third
    return second
print(climbingStairs(5))