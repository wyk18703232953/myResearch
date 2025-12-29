import random

def main(n: int):
    # 1. 生成测试数据
    # 生成一个 n 位数字串（首位不为 0），以及一个上界 b
    if n <= 0:
        return ""
    digits = [str(random.randint(0, 9)) for _ in range(n)]
    if digits[0] == '0':
        digits[0] = str(random.randint(1, 9))
    a = digits[:]  # 字符列表
    # 生成一个上界 b，保证是一个不小于由 a 排序后形成的最小数的随机数
    min_num = int("".join(sorted(a)))
    max_num = int("".join(sorted(a, reverse=True)))
    if min_num == max_num:
        b = max_num
    else:
        b = random.randint(min_num, max_num)

    # 2. 原逻辑
    ans = ""
    a.sort(reverse=True)
    while len(a) > 0:
        for i in range(len(a)):
            num = ans + a[i] + "".join(sorted(a[:i] + a[i+1:]))
            if int(num) <= b:
                ans += a[i]
                a = a[:i] + a[i+1:]
                break

    # 3. 输出结果（可根据需要修改）
    print("digits:", "".join(digits))
    print("b:", b)
    print("answer:", ans)
    return ans

if __name__ == "__main__":
    # 示例：规模为 5 的测试
    main(5)