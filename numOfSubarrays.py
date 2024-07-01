
def numOfSubarrays(nums, k, threshold):
    numOfSubArrays = 0
    L = 0
    sum = 0
    for R in range(len(nums)):

        sum += nums[R]
        print(f"L = {L}, R = {R},  nums[R] = {nums[R]}, nums[L] = {nums[L]}, sum = {sum}, threshold = {threshold}, average = {sum // k}")
        if R >= L + k -1:
            L += 1
            average = int(sum / k)
            if average >= threshold:
                numOfSubArrays += 1
            sum = sum - nums[L-1]
    return numOfSubArrays

nums = [[2,2,2,2,5,5,5,8],[1,1,1,1,1],[11,13,17,23,29,31,7,5,2,3],[7,7,7,7,7,7,7],[4,4,4,4]]
k = [3,1,3,7,4]
threshold = [4,0,3,7,1]
for i in range(len(nums)):
    print(numOfSubarrays(nums[i], k[i], threshold[i]))

    