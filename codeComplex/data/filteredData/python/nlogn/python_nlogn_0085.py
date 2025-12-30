import random

def main(n):
    # 生成测试数据
    # k 在 [1, n] 内随机
    k = random.randint(1, n)
    tm = []

    # 生成 n 组 (p, t)，这里示例使用 1~100 的随机整数
    for _ in range(n):
        p = random.randint(1, 100)
        t = random.randint(1, 100)
        tm.append([p, t])

    # 按原逻辑处理
    tm.sort(key=lambda x: (-x[0], x[1]))
    ans = tm.count(tm[k - 1])
    print(ans)

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)