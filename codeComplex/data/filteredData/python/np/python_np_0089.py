import math
import random


def compute_probability(s1: str, s2: str) -> float:
    dist = 0
    pos = 0
    unrecognized = 0

    for ch in s1:
        if ch == "+":
            dist += 1
        else:
            dist -= 1

    for ch in s2:
        if ch == "+":
            pos += 1
        elif ch == "-":
            pos -= 1
        elif ch == "?":
            unrecognized += 1

    difference = dist - pos

    # 原逻辑：如果差值绝对值大于未知数，概率为 0
    if abs(difference) > abs(unrecognized):
        return 0.0

    extra = unrecognized - abs(difference)

    # 如果 extra 为奇数，也不可能达到目标
    if extra % 2 != 0:
        return 0.0

    # 计算组合数 C(unrecognized, extra/2 + (unrecognized - extra)) 等价于 C(unrecognized, (unrecognized + difference) / 2)
    # 原始写法使用了 perm_extra 再除以两个 factorial，这里保持一致但修正为整数运算
    # extra/2 + (unrecognized - extra) = unrecognized - extra/2
    k = unrecognized - extra // 2
    # C(unrecognized, k)
    perm_extra = math.factorial(unrecognized) / (
        math.factorial(k) * math.factorial(unrecognized - k)
    )
    probability = perm_extra * (0.5 ** unrecognized)
    return float(probability)


def generate_test_data(n: int) -> tuple[str, str]:
    """
    根据规模 n 生成 s1, s2：
    - s1: 长度 n，由 '+' 和 '-' 组成
    - s2: 长度 n，由 '+', '-', '?' 组成
    """
    choices_s1 = ["+", "-"]
    choices_s2 = ["+", "-", "?"]

    s1 = "".join(random.choice(choices_s1) for _ in range(n))
    s2 = "".join(random.choice(choices_s2) for _ in range(n))
    return s1, s2


def main(n: int):
    s1, s2 = generate_test_data(n)
    prob = compute_probability(s1, s2)
    print("{0:.9f}".format(prob))


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)