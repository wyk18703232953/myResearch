import random

def main(n: int):
    # 生成测试数据：1..n 的一个随机排列
    a = list(range(1, n + 1))
    random.shuffle(a)

    a_reverse = a.copy()
    status = []
    for i in range(n):
        a_reverse[a[i] - 1] = i
        status.append(None)

    pos = a_reverse[n - 1]
    status[pos] = False
    fails = set()
    fails.add(pos)

    for i in range(n - 1, 0, -1):
        i_ = i - 1
        pos = a_reverse[i_]
        for k in range((pos + 1) % i - 1, n, i):
            if k == pos:
                continue
            if k in fails:
                status[pos] = True
                break
        if not status[pos]:
            status[pos] = False
            fails.add(pos)

    result = ""
    for i in status:
        if i is True:
            result += "A"
        else:
            result += "B"

    print(result)

if __name__ == "__main__":
    # 示例：调用 main(8)
    main(8)