import random

def solve_one(n, k, a):
    rgb = [0] * n
    gbr = [0] * n
    brg = [0] * n

    # 计算三种模式下每个位置的改动代价
    for i in range(n):
        c = a[i]
        r_pos = i % 3

        # 模式 RGBRGB...
        if r_pos == 0:
            if c != "R":
                rgb[i] += 1
        elif r_pos == 1:
            if c != "G":
                rgb[i] += 1
        else:
            if c != "B":
                rgb[i] += 1

        # 模式 GBRGBR...
        if r_pos == 0:
            if c != "G":
                gbr[i] += 1
        elif r_pos == 1:
            if c != "B":
                gbr[i] += 1
        else:
            if c != "R":
                gbr[i] += 1

        # 模式 BRGBRG...
        if r_pos == 0:
            if c != "B":
                brg[i] += 1
        elif r_pos == 1:
            if c != "R":
                brg[i] += 1
        else:
            if c != "G":
                brg[i] += 1

    # 前缀和
    for i in range(1, n):
        rgb[i] += rgb[i - 1]
        gbr[i] += gbr[i - 1]
        brg[i] += brg[i - 1]

    ans = 10**18
    # 在长度为 k 的所有子串中取最小代价
    for i in range(k - 1, n):
        if i - k == -1:
            cur = min(rgb[i], gbr[i], brg[i])
        else:
            cur = min(
                rgb[i] - rgb[i - k],
                gbr[i] - gbr[i - k],
                brg[i] - brg[i - k],
            )
        if cur < ans:
            ans = cur
    return ans


def main(n):
    """
    n: 规模参数，表示字符串长度。
    自动生成测试数据：
      - k 在 [1, n] 中随机选择
      - 字符串 a 为长度 n 的随机 'R','G','B' 序列
    输出：单个整数答案
    """
    if n <= 0:
        return

    k = random.randint(1, n)
    colors = ['R', 'G', 'B']
    a = ''.join(random.choice(colors) for _ in range(n))

    ans = solve_one(n, k, a)
    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 进行测试
    main(5)