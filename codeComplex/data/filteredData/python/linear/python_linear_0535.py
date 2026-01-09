def main(n):
    # Deterministically generate k and string s based on n
    # Let k be at most 26 and at least 1
    k = max(1, min(26, n if n > 0 else 1))
    # Generate a string of length n using first k uppercase letters cyclically
    s = [chr(ord('A') + (i % k)) for i in range(n)]

    a = ord('A')
    cnt = [0] * k
    for ch in s:
        cnt[ord(ch) - a] += 1
    result = k * min(cnt)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)