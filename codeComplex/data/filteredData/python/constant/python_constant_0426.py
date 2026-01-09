def main(n):
    # Interpret n as the maximum value for original n and m
    # Generate a deterministic pair (orig_n, orig_m) based on n
    if n <= 0:
        return
    orig_n = n
    orig_m = 2 * n  # deterministic choice to scale with n

    n_val, m_val = orig_n, orig_m

    if m_val <= n_val:
        result = (m_val - 1) // 2

    else:
        if (m_val - n_val) in range(1, n_val + 1):
            if (n_val - (m_val - n_val)) % 2 == 0:
                result = (n_val - (m_val - n_val)) // 2

            else:
                result = (n_val - (m_val - n_val)) // 2 + 1

        else:
            result = 0

    # print(result)
    pass
if __name__ == "__main__":
    main(10)