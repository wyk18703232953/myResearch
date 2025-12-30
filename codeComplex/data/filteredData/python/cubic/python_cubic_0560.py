import random

def main(n: int):
    """
    根据规模 n 生成测试数据并执行原逻辑：
    - 生成一个 n 位的数字字符串 a（首位不为 0）
    - 生成一个整数 b，范围设为 [0, 10^n - 1]
    - 按原程序逻辑计算并打印结果
    """
    if n <= 0:
        return

    # 生成 n 位数字字符串 a，首位不为 0
    first_digit = str(random.randint(1, 9))
    other_digits = [str(random.randint(0, 9)) for _ in range(n - 1)]
    a = first_digit + ''.join(other_digits)

    # 生成 b，范围 0 到 10^n - 1
    b = random.randint(0, 10**n - 1)

    # ---- 原逻辑开始 ----
    list_a = list(a)
    list_a.sort()
    max_a = int(''.join(list_a))

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            list_a[i], list_a[j] = list_a[j], list_a[i]
            temp_a = int(''.join(list_a))
            if int(b) < temp_a or temp_a <= max_a:
                list_a[i], list_a[j] = list_a[j], list_a[i]
            else:
                max_a = temp_a

    print(max_a)
    # ---- 原逻辑结束 ----


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)