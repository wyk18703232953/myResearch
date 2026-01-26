def main(n):
    q = n
    results = []
    for i in range(q):
        a = i + 1
        b = 2 * (i + 1)
        c = 3 * (i + 1)
        n_val = a
        m_val = b
        k_val = c
        if max([n_val, m_val]) > k_val:
            results.append(-1)

        else:
            if (n_val + m_val) % 2 == 0:
                if max([n_val, m_val]) % 2 != k_val % 2:
                    results.append(k_val - 2)

                else:
                    results.append(k_val)

            else:
                results.append(k_val - 1)
    return results

if __name__ == "__main__":
    res = main(10)
    for x in res:
        # print(x)
        pass