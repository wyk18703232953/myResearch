import random

def main(n: int):
    # 生成测试数据：随机生成一棵以 1 为根的树
    # fa[i] 表示节点 i 的父亲（1 为根，fa[1]=0）
    fa = [0, 0]  # 占位，让节点从 1 开始，fa[1]=0
    for i in range(2, n + 1):
        fa.append(random.randint(1, i - 1))

    delta = [0] * (n + 1)
    suml = [0] * (n + 1)

    # 原始逻辑
    for i in range(n, 0, -1):
        if suml[i] == 0:
            suml[i] = 1
        delta[suml[i]] += 1
        if fa[i] >= 0:
            suml[fa[i]] += suml[i]

    for i in range(1, n + 1):
        delta[i] += delta[i - 1]

    ans = 0
    for i in range(1, n + 1):
        while ans + 1 <= n and delta[ans] < i:
            ans += 1
        print(f"{ans} ", end="")
    print()

if __name__ == "__main__":
    # 示例调用
    main(10)