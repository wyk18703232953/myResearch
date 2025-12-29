import random

def main(n):
    # 生成测试数据：
    # n 行 (p, t)，其中 p 为评分，t 为时间
    # 同时生成一个 1 <= k <= n
    # 这里仅作为示例，可根据需要调整数据范围
    k = random.randint(1, n)
    lst = []
    for _ in range(n):
        p = random.randint(1, 100)
        t = random.randint(1, 100)
        lst.append([p, -t])

    # 按原逻辑处理
    tmp = sorted(lst, key=lambda x: (x[0], x[-1]), reverse=True)[k - 1]
    result = lst.count(tmp)

    print(result)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)