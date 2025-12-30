import random

mod = 1000000007

def main(n):
    """
    n: 规模，用来生成测试数据的条目数
    """
    # 生成测试数据
    # s 取一个适中范围的随机值
    s = random.randint(1, 10**6)

    # 生成 n 对 (fi, ti)
    # 为了可控，这里让 fi, ti 在 [0, 10^6] 内随机
    pairs = []
    for _ in range(n):
        fi = random.randint(0, 10**6)
        ti = random.randint(0, 10**6)
        pairs.append((fi, ti))

    # 原逻辑封装：根据生成的 s 和 pairs 计算答案
    cm = 0
    for i, (fi, ti) in enumerate(pairs):
        if i == 0:
            cm = fi + ti
        else:
            if fi + ti > cm:
                cm = fi + ti

    if cm > s:
        ans = cm
    else:
        ans = s

    # 输出结果（可以根据需要改为返回结果）
    print(ans)


if __name__ == "__main__":
    # 示例调用：n 为规模
    main(5)