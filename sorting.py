def insertionSort(datalist):
    for i in range(1, len(datalist)):
        j = i
        current = datalist[j]
        while j > 0:
            if current < datalist[j-1]:
                datalist[j] = datalist[j-1]
            else:
                break
            j -= 1
        datalist[j] = current
    return datalist

def insertionSort2(datalist):
    for i in range(1, len(datalist)):
        j = i
        while j > 0:
            if datalist[j] < datalist[j-1]:
                datalist[j], datalist[j-1] = datalist[j-1], datalist[j]
            j -= 1
    return datalist

def selectionSort(datalist):
    for i in range(len(datalist)):
        min_index = i
        for j in range(i+1, len(datalist)):
            if datalist[j] <= datalist[min_index]:
                min_index = j
            j += 1
        datalist[min_index],datalist[i] = datalist[i],datalist[min_index]
    return datalist

def bubbleSort(datalist):
    for i in range(len(datalist)):
        for j in range(len(datalist)-1):
            if datalist[j] > datalist[j+1]:
                datalist[j], datalist[j+1] = datalist[j+1], datalist[j]
    return datalist

def merge(datalist1, datalist2):
    result = []
    i = j = 0
    while i < len(datalist1) and j < len(datalist2):
        if datalist1[i] < datalist2[j]:
            result.append(datalist1[i])
            i += 1
        else:
            result.append(datalist2[j])
            j += 1
    while i < len(datalist1):
        result.append(datalist1[i])
        i += 1
    while j < len(datalist2):
        result.append(datalist2[j])
        j += 1
    return result

def mergeSort(datalist):
    if len(datalist) <= 1:
        return datalist
    mid = len(datalist) // 2
    left = mergeSort(datalist[:mid])
    right = mergeSort(datalist[mid:])
    return merge(left, right)

def quickSort(datalist):
    if len(datalist) <= 1:
        return datalist
    pivot = datalist.pop()
    leftList = []
    rightList = []
    for i in range(len(datalist)):
        if datalist[i] < pivot:
            leftList.append(datalist[i])
        else:
            rightList.append(datalist[i])
    return quickSort(leftList) + [pivot] + quickSort(rightList)

def main():
    #datalist = [1,2,4,8,10,11,12,13,14,20,30,40]
    #datalist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    datalist = [19, 2, 31, 40, 17, 15, 11, 86, 55, 14, 95, 66, 8, 47, 23, 39, 99, 45, 4, 81, 20, 13, 42, 89, 23, 75, 48, 46, 29, 85, 82, 6, 38]
    #print(datalist)
    #print(insertionSort(datalist))
    #print(insertionSort2(datalist))
    #print(selectionSort(datalist))
    #print(bubbleSort(datalist))
    #print(mergeSort(datalist))
    print(quickSort(datalist))

if __name__ == "__main__":
    main()