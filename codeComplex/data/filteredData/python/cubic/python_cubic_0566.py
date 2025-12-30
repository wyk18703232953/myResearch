import random

fre = [0] * 11
c = False
a = ""
b = ""


def DFS(aa, bb):
    global c, fre, a, b
    if aa == len(a):
        print(bb)
        return True  # 找到解，结束搜索
    for i in range(9, -1, -1):
        if (fre[i] > 0 and i <= int(b[aa])) or (fre[i] > 0 and c):
            fre[i] -= 1
            prev_c = c
            if i < int(b[aa]):
                c = True
            if DFS(aa + 1, bb * 10 + i):
                return True
            fre[i] += 1
            c = prev_c
    return False


def main(n):
    """
    n 为规模参数，用来控制生成测试数据的长度。
    这里的策略：
      - 生成长度为 n 的数字串 a（无前导零）
      - 生成长度为 n 或 n+1 的数字串 b，以覆盖两种分支
    """
    global a, b, fre, c

    # 为了可复现，固定随机种子；如不需要可删除下一行
    random.seed(0)

    # 生成长度为 n 的 a，首位非 0
    if n <= 0:
        return
    first_digit_a = random.randint(1, 9)
    other_digits_a = [random.randint(0, 9) for _ in range(n - 1)]
    a = str(first_digit_a) + "".join(str(d) for d in other_digits_a)

    # 随机决定 b 的长度是 n 还是 n+1，以覆盖 if len(b)>len(a) 分支
    if random.choice([True, False]):
        len_b = n + 1
    else:
        len_b = n

    # 生成长度为 len_b 的 b，首位非 0
    first_digit_b = random.randint(1, 9)
    other_digits_b = [random.randint(0, 9) for _ in range(len_b - 1)]
    b = str(first_digit_b) + "".join(str(d) for d in other_digits_b)

    # 重置全局状态
    fre = [0] * 11
    c = False

    # 执行原逻辑
    if len(b) > len(a):
        x = sorted(a)
        print("".join(x[::-1]))
    else:
        for ch in a:
            fre[int(ch)] += 1
        DFS(0, 0)


# 示例调用
if __name__ == "__main__":
    main(5)