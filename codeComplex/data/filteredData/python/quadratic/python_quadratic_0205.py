import random

def main(n: int):
    # 生成测试数据：n 行，每行是长度为 m 的 0/1 字符串
    # 这里约定 m = n，也可以按需修改生成规则
    m = n
    s, l, f = [[] for _ in range(n)], [0] * m, 0

    # 随机生成 0/1 串，逻辑与原程序一致
    for i in range(n):
        # 生成一行长度为 m 的 0/1 字符串
        t = ''.join(random.choice('01') for _ in range(m))
        for j in range(m):
            if t[j] == "1":
                l[j] += 1
                s[i].append(j)

    for i in range(n):
        r = set(l[c] - 1 for c in s[i])
        if 0 not in r:
            f = not f
            break

    print("YNEOS"[not f::2])


if __name__ == "__main__":
    # 示例：n = 5，可自行修改或在外部调用 main(n)
    main(5)