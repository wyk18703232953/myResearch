import random

def main(n: int):
    # n 为测试数据规模，即生成的牌张数
    # 牌的形式与原程序一致：'<数字><花色>'，数字为1-9，花色为'p','m','s'
    s = [0] * 10
    m = [0] * 10
    p = [0] * 10

    # 生成测试数据：长度为 n 的牌序列
    # 例如：["1p", "9m", "3s", ...]
    suits = ['p', 'm', 's']
    D = []
    for _ in range(n):
        num = random.randint(1, 9)
        suit = random.choice(suits)
        D.append(f"{num}{suit}")

    # 原始逻辑
    for i in D:
        if i[1] == 'p':
            p[int(i[0])] += 1
        elif i[1] == 'm':
            m[int(i[0])] += 1
        else:
            s[int(i[0])] += 1

    need = 3
    for i in range(1, 10):
        need = min(3 - p[i], need)
        need = min(3 - s[i], need)
        need = min(3 - m[i], need)
        if i <= 7:
            tmp = 0
            tmp += min(1, p[i])
            tmp += min(1, p[i + 1])
            tmp += min(1, p[i + 2])
            need = min(3 - tmp, need)

            tmp = 0
            tmp += min(1, m[i])
            tmp += min(1, m[i + 1])
            tmp += min(1, m[i + 2])
            need = min(3 - tmp, need)

            tmp = 0
            tmp += min(1, s[i])
            tmp += min(1, s[i + 1])
            tmp += min(1, s[i + 2])
            need = min(3 - tmp, need)

    print(need)


if __name__ == "__main__":
    # 示例：调用 main(13)，可按需修改 n
    main(13)