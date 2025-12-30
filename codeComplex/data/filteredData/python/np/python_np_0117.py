import random

def main(n):
    # 生成规模为 n 的测试数据：n 个随机整数
    # 可按需要修改数据生成方式
    m = n
    inputs = [random.randint(0, 10**9) for _ in range(m)]

    values = []
    idx = []
    for i in range(m):
        x = inputs[i]
        ans = 0
        for j, xx in enumerate(values):
            if (xx ^ x) < x:
                x ^= xx
                ans ^= idx[j]
        if x == 0:
            anss = []
            tmp_ans = ans
            for j in range(i):
                if (tmp_ans & 1) != 0:
                    anss.append(j)
                tmp_ans >>= 1
            # 原逻辑为打印，这里仍然打印结果
            if anss:
                print(len(anss), *anss)
            else:
                print(0)
        else:
            print(0)
            values.append(x)
            idx.append(ans ^ (1 << i))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)