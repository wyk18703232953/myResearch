import random

def main(n):
    """
    n: 生成的牌张数（规模参数）
    牌格式为 '<数字><花色>'，如 '3m', '7p', '9s'
    """
    # 1. 根据 n 生成测试数据
    # 牌面数字 1~9，花色 m, p, s
    tiles = []
    suits = ['m', 'p', 's']
    for _ in range(n):
        num = random.randint(1, 9)
        suit = random.choice(suits)
        tiles.append(f"{num}{suit}")

    # 2. 原逻辑封装
    s = tiles
    hand = {'m': [], 'p': [], 's': []}

    for item in s:
        hand[item[1]].append(int(item[0]))

    min_steps_needed = 10

    for symb in ['m', 'p', 's']:
        hand[symb] = sorted(hand[symb])
        for start in range(1, 10):
            a_needed = 10
            b_needed = 10

            a_needed = 3 - hand[symb].count(start)

            b1, b2, b3 = 0, 0, 0
            if hand[symb].count(start) > 0:
                b1 = 1
            if hand[symb].count(start + 1) > 0:
                b2 = 1
            if hand[symb].count(start + 2) > 0:
                b3 = 1

            b_needed = 3 - b1 - b2 - b3

            if a_needed < min_steps_needed:
                min_steps_needed = a_needed
            if b_needed < min_steps_needed:
                min_steps_needed = b_needed

    print(min_steps_needed)


if __name__ == "__main__":
    # 示例：规模 n=13
    main(13)