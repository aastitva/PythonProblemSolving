def searchMatrix(matrix, target):
    for row in matrix:
        print(row)
        left, right = 0, len(row) - 1
        print(left, right)
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if target == row[mid]:
                return True
            elif target < row[mid]:
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1
    return False

matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]

target=10
print(searchMatrix(matrix, target))