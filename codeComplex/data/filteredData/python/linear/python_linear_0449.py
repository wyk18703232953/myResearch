def main(n):
    # Deterministic generation of test data based on n
    # n controls the length of t; s contains a '*' in the middle
    if n < 2:
        n = 2
    # s will be of length n+1: n characters plus one '*'
    k = n // 2
    front = "".join(chr(ord('a') + (i % 26)) for i in range(k))
    back = "".join(chr(ord('a') + ((k + i) % 26)) for i in range(n - k))
    s = front + "*" + back
    # Construct t so that its first k and last (n-k) characters match front and back
    middle_len = max(0, n - len(front) - len(back) + 2)
    middle = "".join(chr(ord('a') + ((i + 7) % 26)) for i in range(middle_len))
    t = front + middle + back

    if "*" in s:
        front_part, back_part = s.split("*")
        if len(t) >= len(s) - 1 and t.startswith(front_part) and t.endswith(back_part):
            # print("YES")
            pass

        else:
            # print("NO")
            pass

    else:
        # print("YES" if s == t else "NO")
        pass
if __name__ == "__main__":
    main(10)