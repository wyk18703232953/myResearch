import random

def listtostring(li: list) -> str:
    return ''.join(li)

def main(n: int):
    # 生成长度为 n 的数字串 a 和 b，保证 a <= b 位数相同
    # 用 0-9 中的数字随机生成
    a_digits = [str(random.randint(0, 9)) for _ in range(n)]
    b_digits = [str(random.randint(0, 9)) for _ in range(n)]

    # 确保 a <= b（按整数比较）
    a_val = int(listtostring(a_digits))
    b_val = int(listtostring(b_digits))
    if a_val > b_val:
        a_digits, b_digits = b_digits, a_digits

    a = a_digits
    b = b_digits
    n = len(a)

    a.sort()

    for i in range(0, n):
        for j in range(0, n):
            t = a.copy()
            t[i], t[j] = t[j], t[i]
            t_val = int(listtostring(t))
            a_val = int(listtostring(a))
            b_val = int(listtostring(b))
            if a_val <= t_val <= b_val:
                a[i], a[j] = a[j], a[i]

    print(listtostring(a))

if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)