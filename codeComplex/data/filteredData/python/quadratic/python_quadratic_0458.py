def main(n):
    # 生成确定性的输入数组 a，作为 1..n 的排列
    # 这里采用简单的算术变换保证可复现性
    a = [((i * 3 + 1) % n) + 1 for i in range(n)]

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
            result = result + "A"

        else:
            result = result + "B"

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：对不同规模进行调用
    for size in (5, 10, 20):
        main(size)