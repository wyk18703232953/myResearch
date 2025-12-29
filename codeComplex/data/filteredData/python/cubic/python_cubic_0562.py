import random

def main(n: int):
    # 生成规模为 n 的测试数据：
    # 生成一个长度为 n 的数字串 a（首位不为 0，若 n>1）
    # 再生成一个不小于 len(a) 的 b，使得原逻辑有意义
    if n <= 0:
        return

    # 生成 a
    if n == 1:
        a = str(random.randint(0, 9))
    else:
        first_digit = random.randint(1, 9)
        other_digits = [str(random.randint(0, 9)) for _ in range(n - 1)]
        a = str(first_digit) + "".join(other_digits)

    # 生成 b，使得 len(b) >= len(a)，这里简单生成同长度或更长的随机数
    len_b = random.randint(len(a), len(a) + 2)
    if len_b == 1:
        b = str(random.randint(0, 9))
    else:
        first_digit_b = random.randint(1, 9)
        other_digits_b = [str(random.randint(0, 9)) for _ in range(len_b - 1)]
        b = str(first_digit_b) + "".join(other_digits_b)

    # 原逻辑开始
    la = [int(x) for x in a]
    res = []
    la.sort()
    la = la[::-1]
    lb = [int(x) for x in b]
    cnt = [0] * 20

    def check():
        tres = 0
        for x in range(len(res)):
            tres *= 10
            tres += int(res[x])
        return tres <= int(b)

    if len(a) < len(b):
        for i in range(len(la)):
            print(la[i], end='')
        print()
    else:
        for i in range(len(la)):
            cnt[la[i]] += 1
        flag = 0
        for i in range(len(lb)):
            if flag == 0 and cnt[lb[i]]:
                res.append(lb[i])
                cnt[lb[i]] -= 1
            else:
                flag = i - 1
                for j in range(lb[i] - 1, -1, -1):
                    if cnt[j]:
                        res.append(j)
                        cnt[j] -= 1
                        break
                for j in range(9, -1, -1):
                    while cnt[j]:
                        res.append(j)
                        cnt[j] -= 1
                break
        while not check():
            temp = []
            cnt = [0] * 20
            for x in range(flag):
                temp.append(res[x])
                cnt[res[x]] -= 1
            for i in la:
                cnt[i] += 1
            res = temp
            for v in range(lb[flag] - 1, -1, -1):
                if cnt[v]:
                    res.append(v)
                    cnt[v] -= 1
                    break
            for v in range(9, -1, -1):
                while cnt[v]:
                    res.append(v)
                    cnt[v] -= 1
            flag -= 1
        for i in range(len(res)):
            print(res[i], end='')
        print()


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)