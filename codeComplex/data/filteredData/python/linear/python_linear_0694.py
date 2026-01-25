def main(n):
    # 由 n 生成确定性输入：将 n 映射为 (N, v)
    # 保证 1 <= v <= N 且 N >= 1
    if n <= 0:
        N = 1
    else:
        N = n
    v = N // 2 if N // 2 > 0 else 1

    # 原程序核心逻辑
    n_val = N
    v_val = v
    answer = 0
    n_val -= 1
    if n_val <= v_val:
        result = n_val
    else:
        answer = v_val
        for i in range(1, n_val - v_val + 1):
            answer += (i + 1)
        result = answer

    print(result)
    return result


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(10)