import random

def main(n: int):
    # 生成测试数据：随机生成 a、b，规模由 n 控制
    # 让 a 为 n 位数（首位不为 0），b 为 n 位数（可能比 a 大或小）
    if n <= 0:
        return

    # 生成 n 位数的 a
    a_digits = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(n - 1)]
    a = int("".join(map(str, a_digits)))

    # 生成 n 位数的 b
    b_digits = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(n - 1)]
    b = int("".join(map(str, b_digits)))

    # 原逻辑开始
    x = [0] * 10
    ta = a
    while ta:
        x[ta % 10] += 1
        ta //= 10

    ans = 0
    for i in range(9, -1, -1):
        for _ in range(x[i]):
            ans = ans * 10 + i

    if ans <= b:
        print(ans)
        return

    ans = 0
    for ch in str(b):
        c = int(ch)
        while c >= 0 and not x[c]:
            c -= 1
        if c < 0:
            # 回退
            while True:
                x[ans % 10] += 1
                d = ans % 10
                ans //= 10
                flag = 0
                for bb in range(d - 1, -1, -1):
                    if x[bb]:
                        ans = ans * 10 + bb
                        x[bb] -= 1
                        flag = 1
                        break
                if flag:
                    break
            break
        else:
            x[c] -= 1
            ans = ans * 10 + c
            if c < int(ch):
                break

    for j in range(9, -1, -1):
        for _ in range(x[j]):
            ans = ans * 10 + j

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)