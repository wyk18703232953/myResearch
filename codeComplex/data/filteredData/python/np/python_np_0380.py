from itertools import accumulate
from random import randint


def main(n):
    """
    n: 组数 k（原程序中的 k）
    将随机生成 n 组数组，每组长度随机，元素为随机整数。
    返回原程序应输出的字符串。
    """
    # ---------- 1. 随机生成测试数据 ----------
    k = n  # 规模即组数
    # 每组长度 1~n（可按需要调整），元素值在 -10^6 ~ 10^6 之间
    a = []
    for _ in range(k):
        length = randint(1, max(1, n))          # 每组的长度
        arr = [randint(-10**6, 10**6) for _ in range(length)]
        a.append(tuple(arr))

    # ---------- 2. 以下逻辑基本保持原程序，仅去掉 stdin/stdout ----------
    a2ij = {
        aij: (i, j)
        for i, ai in enumerate(a)
        for j, aij in enumerate(ai)
    }

    plena = [0] + list(accumulate(map(len, a)))
    suma = tuple(map(sum, a))
    totala = sum(suma)

    if totala % k != 0:
        return "No\n"
    else:
        needle = totala // k
        mask2i2cp = compute_mask2i2cp(a, a2ij, needle, plena, suma)
        dp = compute_previous_mask(mask2i2cp)
        return build_output(dp, mask2i2cp)


def compute_mask2i2cp(a, a2ij, needle, plena, suma):
    used = [False] * plena[-1]  # 保留原变量，虽然未真正使用
    number_of_masks = 1 << len(a)
    mask2i2cp = [-1] * number_of_masks

    for i, ai in enumerate(a):
        for j, aij in enumerate(ai):
            if not used[plena[i] + j]:
                mask, i2cp = compute_mask_i2cp(a2ij, aij, i, j, needle, suma)
                if i2cp != -1:
                    mask2i2cp[mask] = i2cp

    return mask2i2cp


def build_output(dp, mask2i2cp):
    mask = len(mask2i2cp) - 1

    if dp[mask] == -1:
        return "No\n"
    else:
        answer = [-1] * len(mask2i2cp[dp[mask]])

        while mask > 0:
            current_mask = dp[mask]
            for i, cp in enumerate(mask2i2cp[current_mask]):
                if ((current_mask >> i) & 1) == 1:
                    c, p = cp
                    answer[i] = (c, p)
            mask ^= current_mask

        res_lines = ["Yes"]
        res_lines += ["{} {}".format(c, 1 + p) for c, p in answer]
        return "\n".join(res_lines)


def compute_mask_i2cp(a2ij, aij, i, j, needle, suma):
    i2cp = [-1] * len(suma)
    mask = 0
    current_a = aij
    current_i = i

    try:
        while True:
            next_a = needle - (suma[current_i] - current_a)
            next_i, next_j = a2ij[next_a]

            if ((mask >> next_i) & 1) == 1:
                return mask, -1

            mask |= 1 << next_i
            i2cp[next_i] = (next_a, current_i)

            if next_i == i:
                if next_j == j:
                    return mask, i2cp
                return mask, -1

            if next_i == current_i:
                return mask, -1

            current_a = next_a
            current_i = next_i
    except KeyError:
        return mask, -1


def compute_previous_mask(mask2cp):
    number_of_masks = len(mask2cp)
    dp = [-1] * number_of_masks
    dp[0] = 0

    for mask, cp in enumerate(mask2cp):
        if cp != -1:
            complement_mask = (number_of_masks - 1) & (~mask)
            previous_mask = complement_mask

            while previous_mask > 0:
                if dp[previous_mask] != -1 and dp[previous_mask | mask] == -1:
                    dp[previous_mask | mask] = mask
                previous_mask = (previous_mask - 1) & complement_mask

            if dp[mask] == -1:
                dp[mask] = mask
    return dp


# 示例调用（实际评测时由外部调用 main(n)）
if __name__ == "__main__":
    print(main(3))