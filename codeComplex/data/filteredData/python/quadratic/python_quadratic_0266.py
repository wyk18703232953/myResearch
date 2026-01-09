def main(n):
    # Deterministically generate parameters a, b from n
    # Ensure a, b are positive and small, but vary with n
    a = (n % 3) + 1
    b = ((n // 3) % 3) + 1

    # Core logic from original program
    if min(a, b) > 1:
        return "NO\n"

    M = [[0] * n for _ in range(n)]

    output_lines = []

    if a == 1 and b == 1:
        if n == 1:
            output_lines.append("YES")
            output_lines.append("0")
            return "\n".join(output_lines) + "\n"
        if n == 2 or n == 3:
            return "NO\n"
        for i in range(1, n):
            M[i - 1][i] = 1
            M[i][i - 1] = 1

    else:
        s = n - max(a, b) + 1
        for i in range(s):
            for j in range(s):
                if i != j:
                    M[i][j] = 1
        if a == 1:
            for i in range(n):
                for j in range(n):
                    if i != j:
                        M[i][j] = 1 - M[i][j]

    output_lines.append("YES")
    for i in range(n):
        output_lines.append("".join(map(str, M[i])))

    return "\n".join(output_lines) + "\n"


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    result = main(10)
    # print(result, end="")
    pass