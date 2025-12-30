import random

def main(n):
    # 生成规模为 n 的测试数据
    # 随机生成 k，保证 1 <= k <= n
    k = random.randint(1, n)

    # 生成 n 个 (x, y) 对，范围可自行调节
    arr = []
    for _ in range(n):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        arr.append((x, y))

    # 按原程序逻辑排序
    arr.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    # 找到第 k 个元素
    req = arr[k - 1]

    # 统计与 req 相等的对的数量
    count = 0
    for a in arr:
        if a == req:
            count += 1

    print(count)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)