from itertools import accumulate
from random import randint


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


def compute_mask2i2cp(a, a2ij, needle, plena, suma):
    used = [False] * plena[-1]
    number_of_masks = 1 << len(a)
    mask2i2cp = [-1] * number_of_masks

    for i, ai in enumerate(a):
        for j, aij in enumerate(ai):
            if not used[plena[i] + j]:
                mask, i2cp = compute_mask_i2cp(a2ij, aij, i, j, needle, suma)

                if i2cp != -1:
                    mask2i2cp[mask] = i2cp

                    for cp in i2cp:
                        if cp != -1:
                            c, p = cp
                            ii, jj = a2ij[c]
                            used[plena[ii] + jj] = True
    return mask2i2cp


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


def reconstruct_answer(dp, mask2i2cp):
    mask = len(mask2i2cp) - 1
    if dp[mask] == -1:
        return None

    answer = [-1] * len(mask2i2cp[dp[mask]])

    while mask > 0:
        current_mask = dp[mask]
        for i, cp in enumerate(mask2i2cp[current_mask]):
            if 1 == ((current_mask >> i) & 1):
                c, p = cp
                answer[i] = (c, p)
        mask ^= current_mask

    return answer


def generate_test_data(n):
    """
    根据规模 n 生成测试数据:
    - 组数 k = n
    - 每组长度在 [1, n] 之间
    - 整体构造满足总和可被 k 整除的情况，以便有较大概率存在解
    """
    k = n
    if k <= 0:
        return []

    # 构造 k 组，每组至少一个元素
    groups = []
    base_values = []
    for i in range(k):
        length = randint(1, n)
        group = [randint(-10 * n, 10 * n) for _ in range(length)]
        groups.append(group)
        base_values.append(group[0])

    # 调整第一个元素，保证总和可被 k 整除
    total = sum(sum(g) for g in groups)
    remainder = total % k
    if remainder != 0:
        # 修改第一个元素以补偿 remainder
        groups[0][0] -= remainder
    return tuple(tuple(g) for g in groups)


def main(n):
    """
    n 为规模参数，用于生成测试数据。
    返回值：
      - 若无解: 返回 ("No", None, a)
      - 若有解: 返回 ("Yes", answer, a)
        其中 answer 是长度为 k 的列表，answer[i] = (c, p)
        表示从值 c 所在的组移动到第 i 组，p 为目标组的下标(0-based)。
    """
    # 1. 生成测试数据 a: 元组的元组
    a = generate_test_data(n)
    k = len(a)

    # 建立 value -> (i, j) 的映射（假定值唯一；若不唯一则算法与原题相同地只取最后一次）
    a2ij = {
        aij: (i, j)
        for i, ai in enumerate(a)
        for j, aij in enumerate(ai)
    }

    plena = [0] + list(accumulate(map(len, a)))
    suma = tuple(map(sum, a))
    totala = sum(suma)

    if k == 0 or totala % k != 0:
        return "No", None, a

    needle = totala // k
    mask2i2cp = compute_mask2i2cp(a, a2ij, needle, plena, suma)
    dp = compute_previous_mask(mask2i2cp)
    answer = reconstruct_answer(dp, mask2i2cp)

    if answer is None:
        return "No", None, a
    return "Yes", answer, a


if __name__ == "__main__":
    # 示例运行：规模 n = 4
    status, answer, data = main(4)
    print(status)
    print("data:", data)
    if status == "Yes":
        # 输出与原题类似的形式：每组一行 "c p+1"
        for c, p in answer:
            print(c, p + 1)