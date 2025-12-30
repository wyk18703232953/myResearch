import random

def main(n: int):
    # 生成测试数据：m 为若干倍 n，元素范围为 [1, n]
    # 这里简单设 m = 3 * n，可按需要自行调整
    m = 3 * n
    li = [random.randint(1, n) for _ in range(m)]

    dic = {}
    c = 0
    for i in range(n):
        dic.setdefault(i + 1, 0)
    for i in li:
        if 0 not in dic.values():
            c = c + 1
            for j in range(1, n + 1):
                dic[j] = dic[j] - 1
        dic[i] = dic[i] + 1
    if 0 not in dic.values():
        c = c + 1
    print(c)


if __name__ == "__main__":
    # 示例运行
    main(5)