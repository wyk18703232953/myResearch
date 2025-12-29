import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 l, r
    # 约定：n 表示二进制位数上限
    if n <= 0:
        n = 1
    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(l, max_val)  # 保证 l <= r

    # 原始逻辑开始
    p = bin(l)[2:]
    q = bin(r)[2:]

    t = len(q)
    u = len(p)
    p = (t - u) * '0' + p
    ans = []

    i = 0
    for i in range(len(q)):
        if q[i] == '1' and p[i] == '0':
            ans.append(1)
            break
        elif q[i] == '1' and p[i] == '1':
            ans.append(0)
            continue
        elif q[i] == '0' and p[i] == '1':
            ans.append(1)
            continue
        else:
            ans.append(0)

    for j in range(i + 1, len(p)):
        ans.append(1)

    total = 0
    ans.reverse()

    for i in range(len(ans)):
        total += (1 << i) * ans[i]

    print(total)


if __name__ == "__main__":
    # 示例调用：规模为 10（最多 10 位二进制）
    main(10)