def main(n):
    if n == 0:
        # print(0, 0, 0)
        pass

    else:
        a, b = 0, 1
        # For timing experiments we just run up to n iterations deterministically.
        # Original algorithm assumes n is a Fibonacci number; we preserve the loop logic.
        while a + b != n and a + b <= n and b <= n:
            a, b = b, a + b
        if a + b == n:
            # print(0, a, b)
            pass

        else:
            # print(0, 0, 0)
            pass
if __name__ == "__main__":
    # Example deterministic call for scale n; can be adjusted as needed.
    main(100000)