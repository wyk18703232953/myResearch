def main(n):
    # Interpret n as the magnitude of x and k for scalability
    # Deterministic construction:
    # x grows linearly with n, k grows linearly but differently with n
    x = n
    k = 2 * n + 3

    def po(a, p, m):
        if p == 0:
            return 1
        x_local = po(a, p // 2, m) % m
        x_local = (x_local % m * x_local % m) % m
        if p % 2 == 1:
            x_local = (x_local % m * a % m) % m
        return int(x_local)

    m = 1000000007
    if x == 0:
        result = 0

    else:
        result = ((po(2, k + 1, m) % m * x % m) % m - (po(2, k, m) % m - 1) % m) % m
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)