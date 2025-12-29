import random

def main(n):
    # 生成测试数据：随机生成 m 和 m 条边 (x, y)
    # 这里 m 取 [0, n] 区间内的随机值
    m = random.randint(0, n)
    edges = []
    for _ in range(m):
        # 随机生成 1..n 范围内的点对
        x = random.randint(1, n)
        y = random.randint(1, n)
        edges.append((x, y))

    # 原逻辑与输入的 m、(x, y) 无关，只与 n 有关
    cnt = 0
    ans = []
    for i in range(n):
        if cnt % 2 == 0:
            ans.append("0")
        else:
            ans.append("1")
        cnt += 1

    result = "".join(ans)
    print(result)
    return result, edges  # 如需查看生成的数据，可通过返回值使用


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)