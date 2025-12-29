import random

def main(n: int):
    # 根据规模 n 生成测试数据：长度为 n 的数字串（不含前导限制）
    # 这里随机生成 n 位数字串，字符范围 '0'~'9'
    s = ''.join(str(random.randint(0, 9)) for _ in range(n))

    ans = 0
    r, c = 0, 0
    for ch in s:
        digit = int(ch)
        r += digit
        c += 1
        if digit % 3 == 0 or r % 3 == 0 or c == 3:
            ans += 1
            r, c = 0, 0

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)