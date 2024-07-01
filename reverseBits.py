def reverseBits(n):
    return int(bin(n)[2:].zfill(32)[::-1], 2)

def reverseBits2(n):
    result = 0
    for i in range(32):
        lsb = n & 1
        print(f"lsb : {lsb}")
        n >>= 1
        print(f"n : {n}")
        result <<= 1
        print(format(result, '032b'))
        result |= lsb
        print(format(result, '032b'))
    return result 

def reverseBits3(n):
    result = ""
    bin_str = to_32bit_binary(n)
    print(f"bin_str : {bin_str}")
    for i in range(32):
        result += (bin_str[32-i-1])
    return result, int(result, 2)

def to_32bit_binary(num):
    # Use mask to limit the number to 32 bits
    MASK = 0xFFFFFFFF
    if num < 0:
        # For negative numbers, get the two's complement representation
        num = (num & MASK)
    # Format the number as a 32-bit binary string
    return format(num, '032b')

# Example usage:
num1 = -5
num2 = 3

binary_num1 = to_32bit_binary(num1)
binary_num2 = to_32bit_binary(num2)

print(f"32-bit binary of {num1}: {binary_num1}")
print(f"32-bit binary of {num2}: {binary_num2}")


#print(reverseBits((43261596)))
#print(bin(43261596))
print(reverseBits2((5)))
#print(reverseBits3("00000010100101000001111010011100"))