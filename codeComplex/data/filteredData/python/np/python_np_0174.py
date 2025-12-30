import random

def set_bit(mask, pos):
    return mask | (1 << pos)

def is_on(mask, pos):
    return (mask & (1 << pos)) > 0

def main(n):
    # 根据规模 n 生成测试数据
    # 为了可控，这里生成：
    #   l = 1/4 * (n * avg)
    #   r = 3/4 * (n * avg)
    #   x = avg 差值阈值
    #   dif 为 1..10 之间的随机整数
    random.seed(0)
    dif = [random.randint(1, 10) for _ in range(n)]
    avg = sum(dif) // (n if n > 0 else 1) or 1
    l = max(0, (n * avg) // 4)
    r = (n * avg * 3) // 4 if n > 0 else 0
    x = max(1, avg)

    count = 0
    mask = 0
    max_mask = (1 << n) - 1

    while mask <= max_mask:
        selected = []
        bit = 0
        while bit < n:
            if is_on(mask, bit):
                selected.append(dif[bit])
            bit += 1

        if selected:
            s = sum(selected)
            if l <= s <= r and max(selected) - min(selected) >= x:
                count += 1

        mask += 1

    print(count)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)