import random

def main(n):
    # 生成测试数据
    # 约定：k 为 2 到 n 之间的随机整数（至少为 2，防止除以 0）
    if n < 2:
        raise ValueError("n 必须至少为 2 才能生成合理的测试数据")
    k = random.randint(2, n)
    # 生成 n 个随机整数，范围可根据需要调整
    l = [random.randint(1, 10 * n) for _ in range(n)]

    # 原逻辑开始
    p = []
    a = sorted(l)
    for i in a:
        if i % k == 0:
            if i // k in p:
                pass
            else:
                p.append(i)
        else:
            p.append(i)
    result = len(set(p))
    print(result)
    return result

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)