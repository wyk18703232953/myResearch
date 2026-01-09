def main(n):
    # Interpret n as the length of the string s; fix k as a deterministic function of n
    if n <= 0:
        return
    k = n // 2 + 1  # deterministic choice of k depending on n

    # Deterministically generate s: a periodic pattern over 'a'..'z'
    alphabet = [chr(ord('a') + (i % 26)) for i in range(26)]
    s = ''.join(alphabet[i % 26] for i in range(n))

    start = -1
    i = 0
    j = 1
    prev = 1
    while i < n - 1:
        while j < n:
            if s[i] == s[j]:
                if start == -1:
                    start = j
                    prev = j
                i += 1
                j += 1

            else:
                i = 0
                j = prev + 1
                prev = j
                start = -1
        break
    if start == -1:
        result = s[:n] * k

    else:
        j = n - start
        result = s[:n] + s[j:n] * (k - 1)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)