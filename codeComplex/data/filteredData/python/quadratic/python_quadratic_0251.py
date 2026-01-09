import math

def generate_input(n):
    # Map n to original input structure: single test case with "n a b"
    # Keep original n as size, and deterministically choose a, b
    # Ensure coverage of different branches by simple arithmetic rules
    if n <= 1:
        nn = 1
        a = 1
        b = 1

    else:
        nn = n
        # Cycle through patterns deterministically
        if n % 4 == 0:
            a, b = 1, 1
        elif n % 4 == 1:
            a, b = 2, 1
        elif n % 4 == 2:
            a, b = 1, 2

        else:
            a, b = 2, 2
    return nn, a, b

def main(n):
    n, a, b = generate_input(n)
    if a > 1 and b > 1:
        # In original code this prints 'NO' and exits
        return None
    elif a == b == 1 and (n == 2 or n == 3):
        # In original code this prints 'NO' and exits
        return None

    else:
        c = max(a, b)
        m = [[0] * n for _ in range(n)]
        for i in range(n - c):
            m[i][i + 1] = 1
            m[i + 1][i] = 1
        if b > 1:
            for i in range(n):
                for j in range(n):
                    if i != j:
                        m[i][j] = 1 - m[i][j]
        # Return matrix instead of printing, for deterministic experiments
        return m

if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    result = main(10)
    # Optional: minimal side effect to keep script non-silent
    if result is not None:
        # print(len(result), len(result[0]))
        pass