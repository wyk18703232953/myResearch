import random

def main(n):
    # 生成规模为 n 的测试数据
    # n: 男生人数
    # m: 女生人数（这里设为 n 或 n+1 保证 m >= 1）
    m = max(1, n)  # 简单设定 m = n，保证 m >= 1

    # 生成 bmin: 每个男生的最小要求
    # 生成 gmax: 每个女生的最大承受
    # 确保有一定随机性和可能的多种情况
    random.seed(0)  # 固定种子便于复现，如不需要可去掉
    bmin = [random.randint(1, 100) for _ in range(n)]
    gmax = [random.randint(1, 100) for _ in range(m)]

    # 原逻辑开始
    bmin.sort()
    gmax.sort()

    max_boy = bmin[-1]
    min_girl = gmax[0]
    if max_boy > min_girl:
        print(-1)
    elif max_boy == min_girl:
        bmin.pop()
        out = sum(gmax) + sum(x * m for x in bmin)
        print(out)
    else:
        bmin.pop()
        out = sum(gmax) - min_girl + max_boy
        out += min_girl + bmin[-1] * (m - 1)
        bmin.pop()
        out += sum(x * m for x in bmin)
        print(out)


if __name__ == "__main__":
    # 示例调用，规模可按需修改
    main(5)