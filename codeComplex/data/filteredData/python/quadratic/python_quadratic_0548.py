def main(n):
    # Interpret original two inputs (n, k) as:
    #   original_n = n
    #   k = n // 2   (a deterministic mapping of scale n)
    original_n = n
    k = n // 2

    d = original_n - k
    d = d // 2

    l = []
    current_n = original_n

    while current_n > 0:
        i = min(current_n, d)
        while i > 0:
            l.append('1')
            i -= 1
            current_n -= 1
        if current_n > 0:
            l.append('0')
            current_n -= 1

    result = "".join(l)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)