import random

def main(n):
    # 生成测试数据
    # 规模 n：字符串长度
    # 随机生成若干组测试（这里取 q=5，可按需调整）
    q = 5
    tests = []
    for _ in range(q):
        k = random.randint(1, n)          # 窗口大小 1..n
        S = ''.join(random.choice('RGB') for _ in range(n))
        tests.append((n, k, S))

    # 执行原逻辑
    for n, k, S in tests:
        S_list = list(S)

        # 将字符映射为 0,1,2
        for i in range(n):
            if S_list[i] == "R":
                S_list[i] = 0
            elif S_list[i] == "G":
                S_list[i] = 1
            else:
                S_list[i] = 2

        ANS = 1 << 50

        for mod in range(3):
            SUM = 0
            # 初始化前 k 个的匹配情况
            for i in range(k):
                if S_list[i] % 3 != (mod + i) % 3:
                    SUM += 1

            ANS = min(ANS, SUM)

            # 滑动窗口
            for i in range(k, n):
                if S_list[i - k] % 3 != (mod + (i - k)) % 3:
                    SUM -= 1
                if S_list[i] % 3 != (mod + i) % 3:
                    SUM += 1
                ANS = min(ANS, SUM)

        print(ANS)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)