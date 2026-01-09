def palindrome(s):
    i = 0
    j = len(s) - 1
    p = True
    while i <= j:
        if s[i] != s[j]:
            p = False
            break
        i += 1
        j -= 1
    return p

def main(n):
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    ans = 0
    for i in range(len(s)):
        for j in range(len(s) - 1, i, -1):
            if not palindrome(s[i:j + 1]):
                ans = max(ans, len(s[i:j + 1]))
                break
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)