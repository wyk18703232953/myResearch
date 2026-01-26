def main(n):
    if n % 4 == 2:
        return -1

    # Deterministic hidden array generation for simulation of qry(i)
    # Example: length n, values follow a simple deterministic pattern
    # such that there is at least one i with a[i] == a[i + n//2] when n % 4 != 2
    arr = [(i * 3 + 7) % 1000003 for i in range(n)]

    # Ensure the problem structure: we need some index i where a[i] == a[i + n//2]
    # For determinism, we enforce this at i = 0 when possible
    if n % 2 == 0 and n >= 2:
        arr[0 + n // 2] = arr[0]

    def qry(i):
        return arr[i]

    def qry2(i):
        a_val = qry(i + n // 2) - qry(i)
        return a_val

    if n % 2 == 1 or n < 2:
        return -1

    a = qry2(0)
    lb, rb = 1, n // 2 - 1
    answer = None
    if a == 0:
        answer = 1

    else:
        while lb <= rb:
            mb = (lb + rb) // 2
            b = qry2(mb)
            if b == 0:
                answer = mb + 1
                break
            if (a > 0) == (b > 0):
                lb = mb + 1

            else:
                rb = mb - 1
    return answer


if __name__ == "__main__":
    # Example deterministic call
    n = 8
    res = main(n)
    # print(res)
    pass