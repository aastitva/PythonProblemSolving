def isPalindrome(s):
    L = 0
    R = len(s)-1
    s = s.lower()
    while L <= R:
        if not s[L].isalnum():
            L += 1
            continue
        if not s[R].isalnum():
            R -= 1
            continue
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True

s = ["Was it a car or a cat I saw?", "tab a cat"]
for i in range(len(s)):
    print(f"string : {s[i]} {isPalindrome(s[i])}")