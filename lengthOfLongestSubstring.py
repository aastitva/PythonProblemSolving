def lengthOfLongestSubstring(string):
    L = R = 0
    max_length = 0
    hashset = set()
    for R in range(len(string)):
        while string[R] in hashset:
            hashset.remove(string[L])
            L += 1
        max_length = max(max_length, R - L + 1)
        hashset.add(string[R])
        print(f" L: {L}, R: {R}, max_length: {max_length}, hashset: {hashset}")
    return max_length

string = ["abcabcbb", "bbbbb", "pwwkew", " ", "au", "aab","dvdf","anviaj"]
for i in range(len(string)):
    print(f" string : {string[i]} {lengthOfLongestSubstring(string[i])}")
