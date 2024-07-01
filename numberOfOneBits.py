def numberOfOneBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def countBits(n):
    result = []
    for i in range(n+1):
        count = 0
        while i:
            count += i & 1
            i >>= 1
        result.append(count)
    return result

def countBits2(n):
    result = []
    for i in range(n+1):
        result.append(bin(i).count('1'))
    return result

def countBits3(n):
    result = [0]
    for i in range(1, n + 1):
        result.append(result[i>>1] + (i & 1))
    return result

print(countBits(5))
print(countBits2(5))
print(countBits3(5))
print(countBits(2))
print(countBits2(2))
print(countBits3(2))