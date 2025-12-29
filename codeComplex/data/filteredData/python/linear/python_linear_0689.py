import math
import random


def f(n, k):
    if k == 1:
        return (n * (n + 1)) // 2
    a = math.floor(math.log(n, k))
    b = sum(k ** i for i in range(a + 1))
    c = sum((i + 1) * k ** i for i in range(a + 1))
    if n < b:
        return c - (b - n) * (a + 1)
    else:
        return c + (n - b) * (a + 2)


def main(n):
    # 生成测试数据：随机选择一个可行的 s（如果存在），否则选择一个不可行的 s
    total = (n * (n + 1)) // 2
    min_possible = 2 * n - 1  # 来自原逻辑的可行下界

    # 先尝试构造一个可行的 s
    feasible_s = None
    trials = 50
    for _ in range(trials):
        # 在一个合理范围内随机选 k，并用 f(n, k) 生成候选 s
        k = random.randint(1, max(2, int(n ** 0.5)))
        cand = f(n, k)
        # cand 必须在原程序允许的范围内
        if min_possible <= cand <= total:
            feasible_s = cand
            break

    if feasible_s is not None:
        s = feasible_s
    else:
        # 若没能构造可行 s，则故意生成一个不可行的 s
        # 1/2 概率让 s 太大，1/2 概率让 s 太小
        if random.random() < 0.5:
            s = total + random.randint(1, n)  # 明显大于最大值
        else:
            s = random.randint(0, min_possible - 1)  # 明显小于可行下界

    # 以下逻辑为原代码主体，仅将 input() 替换为生成的 n, s

    if s == (n * (n + 1)) // 2:
        print("Yes")
        a = [str(i + 1) for i in range(n - 1)]
        print(" ".join(a))
        return

    if s > (n * (n + 1)) // 2:
        print("No")
        return

    if s < 2 * n - 1:
        print("No")
        return

    mini = 1
    maxi = n - 1
    curr = 1
    while True:
        a_val, b_val = f(n, curr), f(n, curr + 1)
        if b_val > s:
            mini = curr + 1
            curr = math.ceil((curr + maxi) / 2)
        elif a_val <= s:
            maxi = curr - 1
            curr = (curr + mini) // 2
        else:
            opt = curr + 1
            break

    depths = [0, 1] + [0] * (n - 1)
    ins = 1
    ind = 2
    while True:
        a = min(opt ** (ind - 1), n - ins)
        depths[ind] = a
        ind += 1
        ins += a
        if ins == n:
            break

    base_b = f(n, opt)
    left = s - base_b
    far = ind - 1
    bulk = ind - 1
    if depths[bulk] == 1:
        bulk -= 1

    while left > 0:
        if far + 1 - bulk <= left:
            far += 1
            left -= far - bulk
            depths[far] += 1
            depths[bulk] -= 1
            if depths[bulk] == 1:
                bulk -= 1
        else:
            depths[bulk] -= 1
            depths[bulk + left] += 1
            left = 0

    verts = [None] * far
    sumi = 0
    for i in range(far):
        verts[i] = list(range(sumi + 1, sumi + 1 + depths[i + 1]))
        sumi += depths[i + 1]

    out = ""
    for i in range(1, far):
        for j in range(len(verts[i])):
            out += str(verts[i - 1][j // opt]) + " "

    print("Yes")
    print(out.strip())


if __name__ == "__main__":
    # 示例：调用 main(n)，这里给一个默认 n
    main(10)