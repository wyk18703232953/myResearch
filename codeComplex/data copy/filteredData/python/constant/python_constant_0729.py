def main(n: int):
    """
    对原程序进行参数化：
    - n 作为原代码中的 k 使用
    - 内部生成一个测试规模为 n 的 k 值序列，并分别计算结果
    - 为展示算法逻辑，这里对 k 从 1 到 n 都运行一遍
    返回：长度为 n 的字符串列表，每个元素是对应 k 的答案
    """
    results = []
    for k in range(1, n + 1):
        kk = k  # 保留原始 k
        # 以下为原逻辑，仅将 input() 换成参数 kk
        num_digits = 1
        num_numbers = 9

        kk -= 1
        while kk > num_digits * num_numbers:
            kk -= num_numbers * num_digits
            num_digits += 1
            num_numbers *= 10

        number = 10 ** (num_digits - 1) + kk // num_digits
        index = kk % num_digits
        answer = str(number)[index]
        results.append(answer)

    # 按要求，这里打印输出；也可以仅返回 results 供外部使用
    for ans in results:
        # print(ans)
        pass

    return results


# 示例调用
if __name__ == "__main__":
    # 这里给出一个示例规模 n，可根据需要修改或在外部调用 main(n)
    main(20)