def add(x, j):
    MOD = 1000000007
    x = x % MOD
    j = j % MOD
    return (x + j) % MOD

def main(n):
    if n <= 0:
        return 0

    # Deterministically generate the statements list of length n.
    # Use a simple periodic pattern based on index:
    # even index -> 'f', odd index -> 's'
    statements = ['f' if i % 2 == 0 else 's' for i in range(n)]

    temp = [[0 for _ in range(n)] for _ in range(n)]
    earlier = [[0 for _ in range(n)] for _ in range(n)]
    temp[0][0] = 1
    earlier[0][0] = 1

    j = 1
    while j < n:
        temp[0][j] = 0
        earlier[0][j] = temp[0][j] + earlier[0][j - 1]
        j += 1

    i = 1
    while i < n:
        if statements[i - 1] == 'f':
            j = 1
            while j < n:
                temp[i][0] = 0
                earlier[i][0] = 0
                temp[i][j] = temp[i - 1][j - 1]
                earlier[i][j] = add(earlier[i][j - 1], temp[i][j])
                j += 1
        else:
            j = 0
            while j < n:
                if j == 0:
                    temp[i][j] = earlier[i - 1][n - 1]
                else:
                    temp[i][j] = earlier[i - 1][n - 1] - earlier[i - 1][j - 1]
                earlier[i][j] = add(earlier[i][j - 1], temp[i][j])
                j += 1
        i += 1

    ans = 0
    j = 0
    while j < n:
        ans = add(ans, temp[n - 1][j])
        j += 1

    return ans % (1000000007)

if __name__ == "__main__":
    # Example deterministic calls for experimentation
    print(main(1))
    print(main(5))
    print(main(10))