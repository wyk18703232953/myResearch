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
    if n <= 0:
        return ""
    # 确定性生成长度为 n 的数组 l
    # 模式：l[i] = (i % n) + 1，保证每个位置为 1..n 之间的整数
    l = [(i % n) + 1 for i in range(n)]

    mem = [0 for _ in range(n)]
    ans = ""
    for i in range(n):
        ans += "A" if wins(mem, l, i) else "B"
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做规模实验
    main(10)