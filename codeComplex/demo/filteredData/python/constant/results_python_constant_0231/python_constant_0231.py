def main(n):
    # 根据 n 构造确定性输入数据
    # 映射规则：
    # a, b, x, y, z 都是 n 的简单确定性函数
    a = n
    b = 2 * n
    x = n // 2
    y = n // 3
    z = n // 4

    result = max(0, 2 * x + y - a) + max(0, y + 3 * z - b)
    return result

if __name__ == "__main__":
    # 示例调用
    for n in range(1, 11):
        # print(n, main(n))
        pass