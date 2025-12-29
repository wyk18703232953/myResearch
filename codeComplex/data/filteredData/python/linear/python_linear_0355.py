import random

def main(n: int) -> None:
    # 生成长度为 n 的数字字符串，首位不为 '0'
    if n <= 0:
        print(0)
        return

    first_digit = str(random.randint(1, 9))
    other_digits = ''.join(str(random.randint(0, 9)) for _ in range(n - 1))
    s = first_digit + other_digits

    count = 0
    i = 0

    while i < len(s):
        if int(s[i]) % 3 == 0:
            count += 1
            i += 1
        elif i < len(s) - 1 and (int(s[i:i+2]) % 3 == 0 or int(s[i+1]) % 3 == 0):
            count += 1
            i += 2
        elif i < len(s) - 2 and (
            int(s[i+1:i+3]) % 3 == 0
            or int(s[i:i+3]) % 3 == 0
            or s[i+2] == '0'
        ):
            count += 1
            i += 3
        else:
            i += 1

    print(count)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)