def main(n):
    # Interpret n as the size of arrays c and a (both length n)
    # Deterministic data generation
    m = n
    c = [i % (n + 1) for i in range(n)]
    a = [(i * 2) % (n + 1) for i in range(m)]

    x = 0
    # Use an index instead of pop for better scalability
    a_idx = 0
    a_len = len(a)
    for i in range(n):
        if a_idx >= a_len:
            break
        try:
            if a[a_idx] >= c[i]:
                x += 1
                a_idx += 1
        except IndexError:
            pass
    return x


if __name__ == "__main__":
    # Example call; you can change 10 to other n for experiments
    result = main(10)
    print(result)