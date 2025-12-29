import random

def main(n: int) -> int:
    # 生成长度为 n 的数字串，避免首位为 '0'（与原逻辑更贴近）
    if n <= 0:
        return 0
    first_digit = str(random.randint(1, 9))
    other_digits = ''.join(str(random.randint(0, 9)) for _ in range(n - 1))
    s = first_digit + other_digits

    n = len(s)
    l = [[0, 0, 0] for _ in range(n)]
    ans = 0

    x = int(s[0]) % 3
    if x == 0:
        ans += 1
    else:
        l[0][x] = 1

    for i in range(1, n):
        x = int(s[i]) % 3
        if x == 0:
            ans += 1
            continue

        if l[i - 1][3 - x] > 0:
            ans += 1
            l[i][3 - x] = 0
            l[i][x] = 0
        else:
            if l[i - 1][x] != 0:
                l[i][1] = 1
                l[i][2] = 1
            else:
                l[i][x] = 1

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)