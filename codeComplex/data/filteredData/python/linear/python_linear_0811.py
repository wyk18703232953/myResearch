import random

def main(n: int):
    # 生成规模为 n 的测试数据 a
    # 这里示例使用 0 ~ n 之间的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    d = {}
    for ai in a:
        if ai in d:
            d[ai] += 1
        else:
            d[ai] = 1

    if (max(d.values()) >= 3 or
        (0 in d and d[0] >= 2) or
        list(d.values()).count(2) >= 2):
        print('cslnb')
        return

    for i in d:
        if d[i] == 2 and (i - 1) in d:
            print('cslnb')
            return

    s = sum(a)
    if s >= n * (n - 1) // 2:
        if (s - n * (n - 1) // 2) % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')
    else:
        # 原代码此处为 pass，即无输出
        pass


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)