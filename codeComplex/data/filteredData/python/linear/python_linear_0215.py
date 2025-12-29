import random

def main(n):
    # 随机生成参数 a, b（b 在原代码中未使用，但保留生成以匹配输入格式）
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    # 随机生成 n 组 (x, vx, vy)
    ghosts = []
    for _ in range(n):
        x = random.randint(-10, 10)
        vx = random.randint(-10, 10)
        vy = random.randint(-10, 10)
        ghosts.append((vx, vy))

    speeds = {}
    for vx, vy in ghosts:
        vl = a * vx - vy
        k = vx + a * vy
        ss = speeds.setdefault(vl, {})
        ss[k] = ss.get(k, 0) + 1

    result = 0
    for vl, ss in speeds.items():
        group_size = sum(ss.values())
        for sss in ss.values():
            result += sss * (group_size - sss)

    print(result)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)