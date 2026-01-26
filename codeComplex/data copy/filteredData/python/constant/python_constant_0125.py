def main(n):
    m = str(n)
    cand1 = int(m)
    if len(m) >= 2:
        cand2 = int(m[:-2] + m[-1:])

    else:
        cand2 = int(m)
    if len(m) >= 1:
        cand3 = int(m[:-1]) if len(m) > 1 else int(m)

    else:
        cand3 = int(m)
    return max(cand1, cand2, cand3)

if __name__ == "__main__":
    # 示例：使用 n 的位数规模进行多次实验
    for k in range(1, 6):
        # 构造一个具有 k 位的确定性整数，例如：111...1 (k 个 1)
        n = int("1" * k)
        result = main(n)
        # print(f"n={n}, result={result}")
        pass