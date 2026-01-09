def main(n):
    # n controls the size of strings: |s| ~ n, |t| ~ n or n+1 depending on pattern
    # Deterministic construction:
    # For even n: s contains '*', for odd n: s has no '*'
    # This way we exercise both branches deterministically.

    if n < 2:
        n = 2

    # Build base pattern using lowercase letters
    base = "".join(chr(ord('a') + (i % 26)) for i in range(n))

    if n % 2 == 0:
        # Pattern with '*'
        # front length = n//2 - 1, back length = n - 1 - front_len
        front_len = max(0, n // 2 - 1)
        front = base[:front_len]
        back = base[front_len: n - 1]
        s = front + "*" + back

        # For deterministic experiment: build t in a way that
        # alternates between matching and not matching as n changes
        if (n // 2) % 2 == 0:
            # Construct t that matches the pattern
            t = front + back

        else:
            # Construct t that does not match
            # Change one character in the middle if possible
            if len(back) > 0:
                t = front + back[:-1] + chr(((ord(back[-1]) - ord('a') + 1) % 26) + ord('a'))

            else:
                # If back is empty, modify front
                if len(front) > 0:
                    t = front[:-1] + chr(((ord(front[-1]) - ord('a') + 1) % 26) + ord('a'))

                else:
                    t = "z"  # fallback non-matching

    else:
        # Pattern without '*'
        s = base
        # For odd n: alternate between equal and different t
        if (n // 2) % 2 == 0:
            t = s

        else:
            t = s[:-1] + chr(((ord(s[-1]) - ord('a') + 1) % 26) + ord('a'))

    # Original core logic
    if "*" in s:
        front, back = s.split("*")
        if len(t) >= len(s) - 1 and t.startswith(front) and t.endswith(back):
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