import random

def main(n):
    # 生成测试数据：根据规模 n 生成 [l, r]
    # 这里选择 r 的数量级与 n 相关，l 随机选择在 [0, r] 内
    if n <= 0:
        return 0

    max_bit = min(60, n.bit_length() + 10)  # 控制 r 的大小
    r = random.randint(1, (1 << max_bit) - 1)
    l = random.randint(0, r)

    masks = []
    for i in range(64, -1, -1):
        if (1 << i) > r:
            continue
        masks.append(1 << i)
        x, y = 0, 0
        for k in masks:
            if x < y:
                x += k
            else:
                y += k
        for j in range(64, -1, -1):
            if ((x >> j) & 1) or ((y >> j) & 1):
                continue
            if x + (1 << j) <= r:
                x += (1 << j)
            if y + (1 << j) <= r:
                y += (1 << j)
        if min(x, y) < l or max(x, y) > r:
            masks.pop()
    ans = sum(masks)
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例调用，n 可根据需要修改
    main(1000)