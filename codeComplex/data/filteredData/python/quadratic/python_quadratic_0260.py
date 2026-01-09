def main(n):
    # Deterministic generation of a, b based on n
    # Ensure 1 <= a, b <= n to avoid trivial invalid cases from generation
    if n <= 3:
        a = 1
        b = 1

    else:
        a = (n // 2) if (n // 2) >= 1 else 1
        b = (n // 3) if (n // 3) >= 1 else 1

    # Core logic from original program
    if a > n:
        return "NO"
    if b > n:
        return "NO"
    if a == 1 and b == 1:
        if n == 2 or n == 3:
            return "NO"
    if (n == 1 and a > 1) or (n == 1 and b > 1):
        return "NO"
    if min(a, b) > 1:
        return "NO"

    def check(mat):
        vis = [0] * n
        cnt = 0
        for i in range(n):
            if vis[i] == 0:
                q = [i]
                cnt += 1
                vis[i] = 1
                while q:
                    t = q.pop(0)
                    for j in range(n):
                        if mat[t][j] == 1 and vis[j] == 0:
                            vis[j] = 1
                            q.append(j)
        return cnt

    mat = [[0 for _ in range(n)] for _ in range(n)]
    m = max(a, b)
    j = 1
    for i in range(n):
        if j < n:
            mat[i][j] = 1
            mat[j][i] = 1
        j += 1
    for i in range(m - 1):
        curr = n - i - 1
        for j in range(n):
            if mat[curr][j] == 1:
                mat[curr][j] = 0
                mat[j][curr] = 0

    output_lines = []
    if b == 1:
        output_lines.append("YES")
        for i in range(n):
            output_lines.append("".join(str(x) for x in mat[i]))

    else:
        output_lines.append("YES")
        for i in range(n):
            for j in range(n):
                mat[i][j] = 1 - mat[i][j]
        for i in range(n):
            mat[i][i] = 0
        for i in range(n):
            output_lines.append("".join(str(x) for x in mat[i]))
    return "\n"*0 + "\n".join(output_lines)


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    n = 5
    result = main(n)
    # print(result)
    pass