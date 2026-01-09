def main(n):
    # Generate deterministic s1 and s2 based on n
    # s1 length = n, s2 length = 1 (since original code only uses s2[0])
    if n <= 0:
        s1 = ""
        s2 = "a"

    else:
        # s1 is a sequence of lowercase letters based on i % 26
        s1 = "".join(chr(ord('a') + (i % 26)) for i in range(n))
        # s2[0] is a single character determined by n
        s2 = chr(ord('a') + (n % 26))

    ans = ""
    if s1 and s2:
        ans = s1[0]
        for i in range(1, len(s1)):
            if s1[i] < s2[0]:
                ans += s1[i]

            else:
                break
        ans = ans + s2[0]
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)