def characterReplacement(s, k):
    mostf = 0
    L = 0
    countMap = {}
    for R in range(len(s)):
        countMap[s[R]] = 1 + countMap.get(s[R],0)
        mostf = max(mostf, countMap[s[R]])
        window_size = R - L + 1
        if window_size - mostf > k:
            countMap[s[L]] -= 1
            L += 1

    return R - L + 1


s = ["ABAB", "AABABBA", "AABBB", "AABBBB"]
k = [2, 1, 2, 2]
for i in range(len(s)):
    print(f"string : {s[i]} {characterReplacement(s[i], k[i])}")
