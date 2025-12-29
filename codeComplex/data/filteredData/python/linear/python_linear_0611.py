import random

def main(n: int):
    # 生成测试数据：1..n 的随机排列
    ai = list(range(1, n + 1))
    bi = list(range(1, n + 1))
    random.shuffle(ai)
    random.shuffle(bi)

    ai2 = [0] * (n + 1)
    n2 = 0
    res = []

    for i in range(n):
        num = 0
        if ai2[bi[i]] != 1:
            for j in range(n2, n):
                ai2[ai[j]] = 1
                if ai[j] == bi[i]:
                    num = j + 1 - n2
                    n2 = j + 1
                    break
        res.append(str(num))
    print(" ".join(res))


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)