# Converted version with main(n), no input(), and generated test data.

import random
import string


def original_logic(a_str: str, b: int) -> str:
    """
    Replicates the original algorithm:
    Given string a_str and integer b, construct the largest possible number (as string)
    using all characters of a_str such that the resulting integer <= b.
    """
    a = sorted(a_str)
    a = a[::-1]  # sort descending
    p = ""
    while a:
        for i, z in enumerate(a):
            # Build tentative number:
            # prefix p + chosen digit a[i] + remaining digits sorted ascending
            n = p + a[i] + "".join(sorted(a[:i] + a[i + 1:]))
            if int(n) <= b:
                p += z
                a.pop(i)
                break
    return p


def main(n: int) -> None:
    """
    n controls the scale of the generated test data.
    Example policy:
      - Length of digit string = n
      - Digits randomly chosen from '0'..'9'
      - b is a random integer with up to n digits (and >= 0).
    """
    # 1. Generate a random digit string of length n (avoiding all leading zeros if possible)
    if n <= 0:
        a_str = "0"
    else:
        # Ensure at least one non-zero digit so the string isn't all zeros trivially.
        digits = [random.choice(string.digits) for _ in range(n)]
        if all(d == '0' for d in digits):
            digits[random.randrange(n)] = random.choice("123456789")
        a_str = "".join(digits)

    # 2. Generate b: a non-negative integer with up to n digits
    #    Let b be between 0 and int(max_possible) inclusive,
    #    where max_possible is the number with n '9's.
    max_possible = int("9" * max(n, 1))
    b = random.randint(0, max_possible)

    # Run original logic
    result = original_logic(a_str, b)

    # Output example: you can adjust this format as needed
    print("a_str:", a_str)
    print("b:", b)
    print("result:", result)


if __name__ == "__main__":
    # Example: run with n = 5
    main(5)