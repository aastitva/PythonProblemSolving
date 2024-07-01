def minCostClimbingStairs(cost):
    forMemo = [-1] * (len(cost)+1)
    forMemo[0] = cost[0]
    forMemo[1] = cost[1]
    for i in range(2, len(cost)):
        forMemo[i] = cost[i] + min(forMemo[i-1], forMemo[i-2])
        print(forMemo)
    return min(forMemo[len(cost)-1], forMemo[len(cost)-2])

def minCostClimbingStairs2(cost):
    #forMemo = [-1] * (len(cost)+1)
    prev1 = cost[1]
    prev2 = cost[0]
    for i in range(2, len(cost)):
        curr = cost[i] + min(prev2, prev1)
        prev1 = prev2
        prev2 = curr
    return prev1 if prev1 < prev2 else prev2
   
cost = [10, 15, 20]
print(minCostClimbingStairs(cost)) # 15