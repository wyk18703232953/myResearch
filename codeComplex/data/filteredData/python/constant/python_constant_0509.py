def m(x, y, k):
    d = min(x, y)
    x -= d
    y -= d
    k -= d

    if k - x - y < 0:
        return -1

    else:
        x += y
        if x % 2 > 0 and k % 2 > 0:
            return d + k - 1
        elif x % 2 > 0:
            return d + k - 1
        elif k % 2 > 0:
            return d + k - 2

        else:
            return d + k


def main(n):
    # 解释输入结构：
    # 原程序：第一行是整数 n，表示测试用例数量
    # 每个测试用例一行包含三个整数 x, y, k
    # 这里将 n 映射为测试用例数量
    results = []
    for i in range(n):
        # 确定性生成每个测试用例 (x, y, k)
        # 随着 i 增长，数值规模线性增大
        x = i + 1          # 从 1 开始递增
        y = (i * 2) + 3    # 简单线性关系
        k = (i * 3) + 5    # 简单线性关系
        res = m(x, y, k)
        results.append(res)

    # 为了保留原有的打印行为，这里输出所有结果
    for val in results:
        # print(val)
        pass
if __name__ == "__main__":
    # 示例调用：可以修改 n 以改变输入规模
    main(10)