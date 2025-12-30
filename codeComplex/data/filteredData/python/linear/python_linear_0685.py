import random

def main(n: int):
    # 根据规模 n 生成测试数据：长度为 n 的正整数数组 b
    # 这里简单生成 1~100 之间的随机数，你可以按需调整
    random.seed(0)
    b = [random.randint(1, 100) for _ in range(n)]

    ff = []
    ss = []
    for i in b[::-1]:
        q = i
        f = q // 2
        if q % 2:
            s = f + 1
        else:
            s = f
        if len(ff) == 0:
            ff = [f]
            ss = [s]
        else:
            if f > ff[-1] or s < ss[-1]:
                d = max(f - ff[-1], ss[-1] - s)
                f -= d
                s += d
            ff.append(f)
            ss.append(s)
    print(*(ff[::-1] + ss))


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)