import random

def main(n: int):
    # 生成测试数据
    # n: 游戏数量
    # m: 账单数量，这里设为 n 或 n 左右
    m = n

    # 生成游戏价格列表 c，价格在 1~100 之间递增或不递增均可
    # 为了更贴近一般用例，这里生成非递减序列
    c = sorted(random.randint(1, 100) for _ in range(n))
    # 生成账单列表 a，价格在 1~100 之间
    a = [random.randint(1, 100) for _ in range(m)]

    ans = 0
    i = 0
    for bill in a:
        try:
            # 在 c[i:] 中寻找第一个 <= bill 的游戏
            offset = next(ind for ind, el in enumerate(c[i:]) if el <= bill)
            i += offset + 1
            ans += 1
            if i >= n:
                break
        except StopIteration:
            break

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)