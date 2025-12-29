import random


def vFlip(m):
    return [list(reversed(row)) for row in m]


def hFlip(m):
    return list(reversed(m))


def rotate(m):
    # rotate 90 degrees clockwise
    return [list(row) for row in zip(*reversed(m))]


def check(map1, map2):
    cur = [row[:] for row in map1]  # copy to avoid modifying original
    for _ in range(4):
        if cur == map2:
            return True
        if vFlip(cur) == map2:
            return True
        if hFlip(cur) == map2:
            return True
        if vFlip(hFlip(cur)) == map2:
            return True
        cur = rotate(cur)
    return False


def gen_random_map(n, chars=("0", "1", ".")):
    # generate an n x n random map using given characters
    return [[random.choice(chars) for _ in range(n)] for _ in range(n)]


def main(n):
    # 1. 生成原始测试数据 map1
    map1 = gen_random_map(n)

    # 2. 基于 map1 随机生成 map2
    #    50% 概率让 map2 可由 map1 变换得到，50% 概率为完全随机
    if random.random() < 0.5:
        # 生成一个由 map1 变换得到的 map2（保证答案为 YES）
        cur = [row[:] for row in map1]
        # 随机旋转 0~3 次
        for _ in range(random.randint(0, 3)):
            cur = rotate(cur)
        # 随机选择一种翻转方式（包括不翻转）
        flip_type = random.choice(["none", "v", "h", "hv"])
        if flip_type == "v":
            cur = vFlip(cur)
        elif flip_type == "h":
            cur = hFlip(cur)
        elif flip_type == "hv":
            cur = vFlip(hFlip(cur))
        map2 = cur
    else:
        # 完全随机生成 map2（大概率答案为 NO）
        map2 = gen_random_map(n)

    # 3. 调用 check 判断，并输出结果
    print("YES" if check(map1, map2) else "NO")


if __name__ == "__main__":
    # 示例：可以手动调整 n 的大小进行测试
    main(4)