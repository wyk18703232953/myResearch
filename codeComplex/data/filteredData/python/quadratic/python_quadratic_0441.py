import random

def main(n: int) -> None:
    # 生成长度为 n 的由数字字符组成的测试串 a
    # 保证至少有一个非零数字，避免 sum 恒为 0 的无意义情况
    if n <= 0:
        print("YES")  # 与原逻辑保持兼容：空串时 sum == 0 -> YES
        return

    digits = [str(random.randint(0, 9)) for _ in range(n)]
    if all(d == '0' for d in digits):
        digits[random.randrange(n)] = str(random.randint(1, 9))
    a = "".join(digits)

    # 以下为原逻辑
    total = 0
    for x in a:
        total += int(x)

    ans = "NO"
    if total == 0:
        ans = "YES"

    s = 1
    while s * s <= total and ans == "NO":
        if total % s == 0:
            # 尝试块和为 s
            t = 0
            flag = 0
            for x in a:
                t += int(x)
                if t == s:
                    flag = 1
                if t > s:
                    if flag == 1:
                        flag = 0
                        t = int(x)
                        if t == s:
                            flag = 1
            if t == s and t != total:
                ans = "YES"

            # 尝试块和为 total // s
            t = 0
            flag = 0
            block = total // s
            for x in a:
                t += int(x)
                if t == block:
                    flag = 1
                if t > block:
                    if flag == 1:
                        flag = 0
                        t = int(x)
                        if t == block:
                            flag = 1
            if t == block and t != total:
                ans = "YES"
        s += 1

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)