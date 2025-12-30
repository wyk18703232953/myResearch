import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 l, r
    # 让 l, r 落在 [0, 2^n - 1] 中，且尽量保证 l != r
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(0, max_val)
        if l == r:
            # 简单处理：若相等就把 r 改为另一值
            r = (r + 1) & max_val

    # 原逻辑开始
    ans = 0
    a, b, c = [], [], []
    if l == r:
        print(0)
        return

    for i in range(63, -1, -1):
        if (r ^ l) & (1 << i):
            for j in range(i, -1, -1):
                ans |= 1 << j
            break
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10) 作为规模 10 的测试
    main(10)