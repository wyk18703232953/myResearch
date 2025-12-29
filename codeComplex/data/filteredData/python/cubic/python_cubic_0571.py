import random

def main(n):
    # 1. 生成测试数据
    # 生成一个长度为 n 的数字串（允许前导零）
    digits = [str(random.randint(0, 9)) for _ in range(n)]
    # 生成一个足够大的上界 b，保证存在可行解
    # 把 digits 排序成最大数字，再加上一些余量
    max_num = int(''.join(sorted(digits, reverse=True)))
    b = max_num + random.randint(0, 10**max(1, n//2))

    # 2. 原始逻辑（去掉 input），对生成的测试数据运行
    a = digits[:]  # 使用生成的 digits 作为输入
    a = sorted(a, reverse=True)
    ans = ''
    while len(a) > 0:
        for i in range(len(a)):
            tmp = ans + a[i] + ''.join(sorted(a[:i] + a[i + 1:]))
            if int(tmp) <= b:
                ans += a[i]
                a = a[:i] + a[i + 1:]
                break

    # 输出测试数据和结果，便于验证
    print("digits:", ''.join(digits))
    print("b:", b)
    print("answer:", ans)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)