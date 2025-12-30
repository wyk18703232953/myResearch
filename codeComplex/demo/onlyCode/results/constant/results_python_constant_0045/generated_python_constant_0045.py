import random

def main(n: int) -> None:
    # 原逻辑：判断 n 是否能被列表中的任一“幸运数”整除
    lucky_numbers = [4, 7, 47, 74, 44, 77, 447, 444, 474, 777, 747, 744, 477]
    c = 0
    for x in lucky_numbers:
        if n % x == 0:
            c = 1
            break
    if c == 1:
        print("YES")
    else:
        print("NO")


def generate_test_n() -> int:
    # 根据 lucky_numbers 生成一部分可整除的数，一部分不可整除的数
    lucky_numbers = [4, 7, 47, 74, 44, 77, 447, 444, 474, 777, 747, 744, 477]
    # 50% 概率生成可整除的 n，50% 概率生成不可整除的 n
    if random.random() < 0.5:
        base = random.choice(lucky_numbers)
        k = random.randint(1, 1000)
        return base * k
    else:
        # 随机生成一个大于 1 的整数，直到它不能被任何幸运数整除
        while True:
            n = random.randint(2, 10_000)
            if all(n % x != 0 for x in lucky_numbers):
                return n


if __name__ == "__main__":
    # 示例：自动生成一个规模 n 并调用 main
    n = generate_test_n()
    main(n)