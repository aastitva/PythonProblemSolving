def getSum(num1,num2):
    max = 0x7FFFFFFF
    mask = 0xFFFFFFFF
    while num2 != 0:
        carry = (num1 & num2) & mask
        num1 = (num1 ^ num2) & mask
        num2 = (carry << 1) & mask
    return num1 if num1 <= max else ~(num1 ^ mask)
    

num1 = -1
num2 = 1
print(getSum(num1,num2))