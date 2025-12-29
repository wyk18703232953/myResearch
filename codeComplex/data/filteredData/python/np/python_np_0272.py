import random

def main(n):
    # 随机生成 q（操作次数），例如 1 到 n 之间
    q = max(1, min(n, 10))  # 为避免过大，这里限制最多 10 组测试，可按需调整

    par = n // 2 + 1
    par = len(list(bin(par)[2:]))

    for _ in range(q):
        # 生成 ui：1 到 n 之间
        ui = random.randint(1, n)

        # 生成操作串 si：长度 1 到 par 之间，由 U/L/R 组成
        ops_len = random.randint(1, par)
        si = ''.join(random.choice('ULR') for _ in range(ops_len))

        temp = bin(ui)[2:]
        now = len(temp)
        num = list((par - now) * "0" + temp)
        now = par - now

        for i in range(len(num)):
            if str(num[i]) == '1':
                now = i

        for ch in si:
            if ch == "U":
                if now == 0:
                    continue
                num[now] = 0
                now -= 1
                num[now] = 1
            elif ch == "L":
                if str(num[-1]) == '1':
                    continue
                num[now] = 0
                now += 1
                num[now] = 1
            else:  # 'R'
                if str(num[-1]) == '1':
                    continue
                now += 1
                num[now] = 1

        for i in range(par):
            num[i] = str(num[i])
        print(int("".join(num), 2))


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此处修改
    main(100)