import random

def main(n):
    # 生成测试数据：n 堆石子，非负整数
    # 这里生成 [0, 10^6] 范围的随机值，可根据需要调整
    piles = [random.randint(0, 10**6) for _ in range(n)]

    piles.sort()
    num = piles[0]
    count = 1
    two = 0
    two_num = 0

    for i in range(1, n):
        if piles[i] == num:
            count += 1
        else:
            if count > 2:
                print('cslnb')
                return
            elif count == 2:
                two_num = num
                two += 1
            num = piles[i]
            count = 1

    if count == 2:
        two_num = num
        two += 1
    if count > 2:
        print('cslnb')
        return
    if two > 1:
        print('cslnb')
        return

    if two == 1:
        if (two_num - 1) in piles:
            print('cslnb')
            return

    if n >= 2:
        if piles[0] == piles[1] and piles[0] == 0:
            print('cslnb')
            return

    moves = 0
    curr = 0
    for i in range(n):
        if piles[i] >= curr:
            moves += piles[i] - curr
            piles[i] = curr
            curr += 1

    for i in piles:
        if i > 0:
            moves += 1
            break

    if n == 1:
        moves += 1

    if moves % 2 != 0:
        print('cslnb')
    else:
        print('sjfnb')


# 示例：调用 main(5)
if __name__ == "__main__":
    main(5)