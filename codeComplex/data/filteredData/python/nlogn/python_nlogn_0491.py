import random

def main(n, seed=0):
    random.seed(seed)

    # 生成测试数据：
    # m 为目标上限，随机在 [1, 10*n] 内
    m = random.randint(1, 10 * n)

    # 生成 n 对 (l, r)，l, r 在 [0, 100] 内
    lr_pairs = []
    for _ in range(n):
        l = random.randint(0, 100)
        r = random.randint(0, 100)
        lr_pairs.append((l, r))

    # 原逻辑开始
    ans = 0
    temp = [0 for _ in range(n)]
    for i in range(n):
        l, r = lr_pairs[i]
        ans += l
        temp[i] = l - r
    temp.sort(reverse=True)

    if ans <= m:
        print(0)
    else:
        for i in range(n):
            ans -= temp[i]
            if ans <= m:
                print(i + 1)
                break
        else:
            print(-1)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)