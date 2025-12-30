import random

def main(n):
    """
    n: 生成的牌数量（规模）
    逻辑：模拟原代码的麻将牌计算，自动生成 n 张牌作为测试数据。
    """
    # 生成测试数据：随机生成 n 张不同格式为 "数字"+"m/p/s" 的牌
    # 数字 1~9，花色 m/p/s
    suits = 'mps'
    tiles = [f"{d}{s}" for d in range(1, 10) for s in suits]
    random.shuffle(tiles)
    # 若 n 大于全部可用牌数，则截断到最大 27（9*3）
    n = min(n, len(tiles))
    a = tiles[:n]

    st = set()
    cnt = [[0 for _ in range(9)] for _ in range(3)]
    for e in a:
        cnt['mps'.index(e[1])][int(e[0]) - 1] = 1
        st.add(e)

    answ = len(st) - 1
    for i in range(3):
        for j in range(7):
            answ = min(answ, 3 - sum(cnt[i][j:j + 3]))
    print(answ)


if __name__ == "__main__":
    # 示例调用，可自行修改 n 测试
    main(5)