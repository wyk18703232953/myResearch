def main(n):
    # n controls the length of the string s
    if n <= 0:
        return 0
    # determine k as number of distinct letters used
    k = min(26, max(1, n // 3 + 1))
    a = ord('A')
    # deterministically generate string s of length n using first k letters
    s = [chr(a + (i % k)) for i in range(n)]
    cnt = [0] * k
    for ch in s:
        cnt[ord(ch) - a] += 1
    result = k * min(cnt)
    print(result)
    return result

if __name__ == "__main__":
    main(100)