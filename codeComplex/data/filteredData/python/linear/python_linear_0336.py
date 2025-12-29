import random

def main(n):
    # 生成测试数据
    # k 取 1~10 之间的随机整数
    k = random.randint(1, 10)
    # 生成递增的坐标数组 l，保证相邻差值 >= 1
    l = [0]
    for _ in range(1, n):
        l.append(l[-1] + random.randint(1, 10))

    # 原始逻辑
    o = 2
    for i in range(n):
        if i + 1 == n:
            break

        d = abs(l[i] - l[i + 1]) / k
        if d == 2:
            o += 1
        elif d > 2:
            o += 2

    print(o)


if __name__ == "__main__":
    # 示例：调用 main，规模设为 5
    main(5)