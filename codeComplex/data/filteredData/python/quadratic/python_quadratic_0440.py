import random

def main(n: int):
    # 生成长度为 n 的数字串作为测试数据（不含前导零）
    if n <= 0:
        print("NO")
        return

    # 生成随机数字串，首位避免为 '0'
    first_digit = str(random.randint(1, 9))
    other_digits = ''.join(str(random.randint(0, 9)) for _ in range(n - 1))
    s = first_digit + other_digits

    # 原逻辑
    for target_sum in range(9 * n + 1):
        cnt = 0
        cursum = 0
        for ch in s:
            cursum += int(ch)
            if cursum == target_sum:
                cnt += 1
                cursum = 0

        if cursum == 0 and cnt > 1:
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    # 示例：规模为 5 时运行一遍
    main(5)