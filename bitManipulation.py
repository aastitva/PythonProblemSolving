# Positive integer
positive_number = 5
print(f"Binary of {positive_number}: {bin(positive_number)}")

# Negative integer
negative_number = -5
print(f"Binary of {negative_number}: {bin(negative_number)}")  # 2's complement representation
print(f"Binary of {negative_number}: {bin(negative_number & 0xff)}")  # 8-bit representation

# Function to get the two's complement representation
def to_twos_complement(value, bits):
    if value < 0:
        print(f"Value1: {1 << 4}")
        value = (1 << bits) + value
        print(f"Value: {value}")
    return value

# Example for -5 in 16-bit representation
negative_number = -5
bits = 16
twos_complement_representation = to_twos_complement(negative_number, bits)
print(f"{negative_number} in {bits}-bit two's complement: {bin(twos_complement_representation)}")

# Breaking down -5
# Step 1: 5 in binary: 0000 0000 0000 0101
# Step 2: Invert bits:  1111 1111 1111 1010
# Step 3: Add 1:       1111 1111 1111 1011

