import random

def main(n):
    # 根据规模 n 生成测试数据
    # 设计：让 m 与 n 同阶，例如 m = 3n，元素值在 [1, 100] 范围内
    m = 3 * n
    a = [random.randint(1, 100) for _ in range(m)]

    dic = {}
    for x in a:
        dic[x] = dic.get(x, 0) + 1

    # 原逻辑：枚举 i，从 1 到 101（含），找到第一个 r < n 的 i，然后输出 i-1
    for i in range(1, 102):
        r = 0
        for val in dic.values():
            r += val // i
        if r < n:
            print(i - 1)
            break


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)