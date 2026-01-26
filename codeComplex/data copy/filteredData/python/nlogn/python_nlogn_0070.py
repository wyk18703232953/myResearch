def main(n):
    # Generate deterministic input: list length = n, values derived from index
    # Example: l[i] = (i % 10) + 1 to keep numbers small but non-trivial
    l = [(i % 10) + 1 for i in range(n)]

    b_sum = 0
    l.sort()
    for i in l:
        b_sum += i

    m_sum = 0
    c = 0
    for i in l[::-1]:
        m_sum += i
        c += 1
        if m_sum > (b_sum / 2):
            break
    # print(c)
    pass
if __name__ == "__main__":
    main(10)