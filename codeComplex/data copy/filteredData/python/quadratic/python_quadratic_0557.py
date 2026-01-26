def main(n):
    # Interpret n as both dimensions of the original problem: n rows and n columns
    rows = n
    cols = n
    n_val = rows
    m_val = cols

    output_lines = []

    for i in range(1, n_val // 2 + 1):
        for j in range(1, m_val + 1):
            output_lines.append(f"{i} {j}")
            output_lines.append(f"{n_val - i + 1} {m_val - j + 1}")

    if n_val % 2 == 1:
        mid_row = n_val // 2 + 1
        for j in range(1, m_val // 2 + 1):
            output_lines.append(f"{mid_row} {j}")
            output_lines.append(f"{mid_row} {m_val - j + 1}")

        if m_val % 2 == 1:
            output_lines.append(f"{mid_row} {m_val // 2 + 1}")

    # Join once for efficiency and determinism
    result = "\n".join(output_lines)
    if result:
        # print(result)
        pass
if __name__ == "__main__":
    # Example deterministic call; change the argument to test other scales
    main(5)