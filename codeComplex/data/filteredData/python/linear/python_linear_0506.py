import random

def wins(mem, l, pos):
    if mem[pos] != 0:
        return mem[pos] == 1

    val = l[pos]

    lo = pos - val
    while lo >= 0:
        if l[lo] > val and not wins(mem, l, lo):
            mem[pos] = 1
            return True
        lo -= val

    hi = pos + val
    while hi < len(l):
        if l[hi] > val and not wins(mem, l, hi):
            mem[pos] = 1
            return True
        hi += val

    mem[pos] = 2
    return False


def main(n):
    # 根据 n 生成测试数据，这里生成 1..n 范围内的随机数
    random.seed(0)
    l = [random.randint(1, n) for _ in range(n)]

    mem = [0 for _ in range(n)]
    ans = ""
    for i in range(n):
        ans += "A" if wins(mem, l, i) else "B"

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)