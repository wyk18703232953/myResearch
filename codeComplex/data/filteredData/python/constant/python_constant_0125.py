import random

def main(n: int):
    # 生成一个 n 位的随机正整数，最高位不为 0
    if n <= 0:
        return
    first_digit = random.randint(1, 9)
    other_digits = [str(random.randint(0, 9)) for _ in range(n - 1)]
    m = str(first_digit) + ''.join(other_digits)

    # 原逻辑迁移：对字符串 m 计算三种情况的最大值
    # 1. 原数
    # 2. 去掉倒数第二位（m[:-2] + m[-1:]）
    # 3. 去掉最后一位（m[:-1]）
    res = max(
        int(m),
        int(m[:-2] + m[-1:]) if len(m) >= 2 else int(m),
        int(m[:-1]) if len(m) >= 1 else int(m)
    )

    print(res)

if __name__ == "__main__":
    # 示例：生成一个 5 位数并执行逻辑
    main(5)