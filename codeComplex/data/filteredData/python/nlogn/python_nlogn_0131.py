import random

def main(n: int):
    # 生成测试数据
    # f: 滤波器数量
    # d: 目标插孔数
    # s: 初始插孔数
    #
    # 这里构造一个合理的规模：
    # f 与 n 同规模，d 和 s 在 [1, 2n] 范围内
    f = n
    d = random.randint(1, 2 * n)
    s = random.randint(1, 2 * n)

    # 每个滤波器增加的插孔数为 filters[i]，取值在 [1, 10]
    filters = [random.randint(1, 10) for _ in range(f)]

    # 原逻辑
    filters.sort(reverse=True)

    freeSockets = s
    usedFilters = 0
    for i in range(len(filters)):
        if freeSockets >= d:
            break
        usedFilters += 1
        freeSockets += filters[i] - 1

    if freeSockets >= d:
        print(usedFilters)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)