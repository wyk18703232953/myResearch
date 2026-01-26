def main(n):
    # Deterministic data generation:
    # Original program reads two integers: n, k
    # Here we treat the function argument `n` as the original `n`
    # and generate a deterministic k based on n.
    original_n = n
    k = n // 2 + 1  # deterministic mapping from n to k

    # Core logic from original program
    a_n = original_n
    a_k = k
    i = 1
    count = 0
    cursum = 0
    while count < a_n:
        if cursum < a_k:
            cursum += i

        else:
            break
        count += 1
        i += 1
    count += cursum - a_k
    if a_n == count:
        result = cursum - a_k

    else:
        ans = cursum - a_k
        extra = 0
        while count < a_n:
            extra += i
            count += (i + 1)
            i += 1
        result = ans + extra
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(1000)