def main(n):
    # Interpret input structure: two integers n, e
    # Map given n to original n and e deterministically
    original_n = n
    e = n // 2  # deterministic mapping
    n = original_n

    d = (n - e) // 2
    q = []
    while n > 0:
        i = min(n, d)
        while i > 0:
            q.append('1')
            i -= 1
            n -= 1
        if n > 0:
            q.append('0')
            n -= 1

    result = "".join(q)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example call; you can change 10 to other n for experiments
    main(10)