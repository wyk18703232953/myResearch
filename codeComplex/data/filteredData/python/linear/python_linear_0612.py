import random

def main(n: int):
    # 生成测试数据：a 为 1..n 的随机排列，b 为 a 的随机排列
    a = list(range(1, n + 1))
    b = a[:]
    random.shuffle(a)
    random.shuffle(b)

    ha = {}
    for i in range(n):
        ha[a[i]] = i

    removed = 0
    out_parts = []
    for i in range(n):
        pos = ha[b[i]]
        if pos < removed:
            out_parts.append("0")
        else:
            out_parts.append(str(pos - removed + 1))
            removed = pos + 1

    print(" ".join(out_parts))


if __name__ == "__main__":
    main(10)