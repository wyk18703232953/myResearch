import random

def main(n):
    # 生成参数 t 和 n 条线段数据
    # t 为间隔阈值，这里取 [1, 10] 的随机整数
    t = random.randint(1, 10)

    # 生成 n 个区间的中心和长度
    # 中心在 [0, 100] 内，长度在 (0, 20] 内
    cont = []
    for _ in range(n):
        hCenter = random.uniform(0, 100)
        hLen = random.uniform(0.1, 20)
        cont.append([hCenter - hLen / 2, hCenter + hLen / 2])

    # 原逻辑
    cont.sort(key=lambda item: item[0])
    ans = 2
    for i in range(n - 1):
        gap = cont[i + 1][0] - cont[i][1]
        if gap > t:
            ans += 2
        elif gap == t:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此修改
    main(5)