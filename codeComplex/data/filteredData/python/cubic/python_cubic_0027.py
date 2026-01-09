def main(n):
    s = ''.join(chr(97 + (i % 26)) for i in range(n))
    ans = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            cur = s[i:j]
            if cur in s[:(j - 1)] or cur in s[(i + 1):]:
                ans = max(ans, j - i)
    return ans

if __name__ == "__main__":
    # print(main(10))
    pass