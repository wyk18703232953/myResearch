def main(n):
    # Interpret n as the number of distinct letters we want in the string s
    # k will be chosen as min(n, 26) to ensure it's meaningful and within 1..26
    if n <= 0:
        # No meaningful input, emulate impossible case
        print(-1)
        return

    k = n if n <= 26 else 26

    # Generate a deterministic string s with exactly min(n, 26) distinct letters
    # Use 'a', 'b', 'c', ... in order, and repeat them to form length n
    distinct_count = n if n <= 26 else 26
    base_letters = [chr(ord('a') + i) for i in range(distinct_count)]
    s_chars = []
    for i in range(n):
        s_chars.append(base_letters[i % distinct_count])
    s = "".join(s_chars)

    a = [0] * 26
    for ch in s:
        idx = ord(ch) - ord('a')
        if 0 <= idx < 26:
            a[idx] = 1

    ans = 0
    i = 0
    while i < 26:
        if a[i] > 0:
            ans += i + 1
            k -= 1
            i += 1
            if k == 0:
                print(ans)
                break
        i += 1
    else:
        print(-1)


if __name__ == "__main__":
    # Example deterministic run with n = 10
    main(10)