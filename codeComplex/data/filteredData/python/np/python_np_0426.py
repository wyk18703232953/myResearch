import random

def main(n):
    # 生成测试数据：
    # n 行，每行 m 个整数（0~1e9之间），这里 m 固定为 9（因为原程序 powls 为 2^0..2^9 共10位，
    # 但 twodarray 长度为 257，仅支持最多 8~9 位，这里用 m=9 保证不越界）
    m = 9
    # 随机数据（可按需要修改为特定生成规则）
    arrmv = [
        [random.randint(0, 10**9) for _ in range(m)]
        for _ in range(n)
    ]

    x = 0
    y = int(1e9 + 1)
    sucls = [0, 0]

    tols = []
    powls = [int(2 ** i) for i in range(10)]
    # twodarray 下标最大为 2^m-1，这里 m<=9，2^9=512，可根据需要调大，这里保持与原程序一致 257
    twodarray = [0 for _ in range(257)]

    while x + 1 < y:
        mid = x + (y - x) // 2
        # 重置 twodarray
        for idx in range(len(twodarray)):
            twodarray[idx] = 0
        tols.clear()

        # 对每一行生成掩码
        for topidx, eletop in enumerate(arrmv):
            tmp = 0
            for idx, ele in enumerate(eletop):
                if idx >= len(powls):
                    break
                if ele >= mid:
                    tmp += powls[idx]

            if tmp < len(twodarray) and not twodarray[tmp]:
                twodarray[tmp] = 1
                tols.append((tmp, topidx))

        sz = len(tols)
        suc = 0
        no = int(2 ** m)
        for i in range(sz):
            for j in range(i, sz):
                if (tols[i][0] | tols[j][0]) == no - 1:
                    sucls[0], sucls[1] = tols[i][1], tols[j][1]
                    suc = 1
                    break
            if suc:
                break

        if suc:
            x = mid
        else:
            y = mid

    # 输出答案（1-based 下标）
    print(sucls[0] + 1, sucls[1] + 1)


if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)