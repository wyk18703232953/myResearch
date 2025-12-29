import random
import string

def main(n):
    # 1. 生成测试数据
    # 生成长度为 n 的数字字符列表（允许重复）
    a = [random.choice(string.digits) for _ in range(n)]
    a_sorted = sorted(a)

    # 生成一个整数 b，范围为 [0, 10^n - 1]
    # 避免 10**n 太大时溢出内存，仅作为上界随机
    if n <= 18:  # 防止超出普通整数使用场景
        max_val = 10 ** n - 1
    else:
        # 对于特别大的 n，用一个限定的上界
        max_val = 10 ** 18 - 1
    b = random.randint(0, max_val)

    # 2. 原逻辑（去掉 input，改为使用上述生成的数据）
    a_list = a_sorted[::-1]  # 对应 a=a[::-1]
    p = ""

    while a_list:
        for i, z in enumerate(a_list):
            candidate = p + a_list[i] + "".join(sorted(a_list[:i] + a_list[i+1:]))
            # 如果 candidate 超过 b 的位数，提前判定为大于 b
            if len(candidate) > len(str(b)):
                continue
            if int(candidate) <= b:
                p += z
                a_list.pop(i)
                break

    # 输出结果以方便验证
    print("Generated digits (sorted ascending):", ''.join(a_sorted))
    print("b:", b)
    print("Result p:", p)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可调
    main(5)