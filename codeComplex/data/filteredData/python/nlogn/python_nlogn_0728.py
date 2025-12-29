import random

def main(n):
    """
    n 作为规模参数：
    - 若 n < 3，则统一生成 3 张牌
    - 若 n >= 3，则生成 n 张牌，但算法仍只取前 3 张参与计算
    """
    # 生成测试数据：n 张牌，每张牌为 "数字(1-9)+花色(m,p,s)"
    if n < 3:
        n = 3
    suits = ['m', 'p', 's']
    cards = []
    for _ in range(n):
        num = random.randint(1, 9)
        suit = random.choice(suits)
        cards.append(f"{num}{suit}")

    # 只取前 3 张牌，完全复现原始逻辑
    t = cards[:3]
    t.sort()

    if t.count(t[0]) == 3:
        ans = '0'
    elif t.count(t[0]) == 2 or t.count(t[1]) == 2:
        ans = '1'
    else:
        num = list(map(int, [t[0][0], t[1][0], t[2][0]]))
        suit = [t[0][1], t[1][1], t[2][1]]
        if len(set(suit)) == 3:
            ans = '2'
        elif len(set(suit)) == 1:
            if num[1] == num[0] + 1 or num[2] == num[1] + 1:
                if num[2] == num[0] + 2:
                    ans = '0'
                else:
                    ans = '1'
            elif num[1] == num[0] + 2 or num[2] == num[1] + 2:
                ans = '1'
            else:
                ans = '2'
        else:
            if suit[0] == suit[1]:
                if num[1] - num[0] in [1, 2]:
                    ans = '1'
                else:
                    ans = '2'
            elif suit[1] == suit[2]:
                if num[2] - num[1] in [1, 2]:
                    ans = '1'
                else:
                    ans = '2'
            else:
                if num[2] - num[0] in [1, 2]:
                    ans = '1'
                else:
                    ans = '2'

    # 输出结果：先输出生成的牌，再输出答案，便于调试/验证
    print("cards:", " ".join(t))
    print(ans)


if __name__ == "__main__":
    # 示例：用规模 5 运行一次
    main(5)