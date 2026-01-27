def main(n):
    t = n
    results = []
    for case_idx in range(1, t + 1):
        a = case_idx
        b = 2 * case_idx + 1
        n_val, m_val = sorted((a, b))
        count = 0
        while n_val > 0:
            count += m_val // n_val
            m_val = m_val % n_val
            n_val, m_val = sorted((n_val, m_val))
        results.append(count)
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)