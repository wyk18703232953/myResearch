import random

def main(n):
    # 生成测试数据
    # t：间隔阈值，取 1~10 之间的随机整数
    t = random.randint(1, 10)
    cont, ans = [], 2

    # 生成 n 段区间，中心在 0~100，长度在 1~20
    for _ in range(n):
        hcenter = random.uniform(0, 100)
        hlen = random.uniform(1, 20)
        cont.append([hcenter - hlen / 2, hcenter + hlen / 2])

    # 逻辑处理
    cont.sort(key=lambda item: item[0])
    for i in range(n - 1):
        gap = cont[i + 1][0] - cont[i][1]
        if abs(gap - t) < 1e-9:  # 浮点判断等于 t
            ans += 1
        elif gap > t:
            ans += 2

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)