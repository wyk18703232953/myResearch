import sys
from collections import defaultdict

def main(n):
    out = sys.stdout

    # 使用 n 作为测试组数 t
    t = n
    while t:
        # 为每组数据构造规模为 n 的数组
        size = n if n > 0 else 1
        # 构造确定性的数组，包含重复元素以满足可能的 4 个或 2+2 情况
        # 模式：[(i % max(1, n//3)) + 1 for i in range(size)]
        base = max(1, n // 3)
        ls = [(i % base) + 1 for i in range(size)]

        dic = defaultdict(lambda: 0, {})
        ls = list(sorted(ls, reverse=True))
        st = set()

        f = 1
        for i in ls:
            dic[i] += 1
            if dic[i] == 4:
                f = 0
                # out.write(str(i) + " " + str(i) + " " + str(i) + " " + str(i) + "\n")
                break
        if not f:
            t -= 1
            f = 1
            continue
        for i in ls:
            if dic[i] >= 2:
                st.add(i)
        st = list(sorted(st, reverse=True))
        ln = len(st)
        if ln < 2:
            # 若不足以构成矩形，则退化为使用最大值重复
            if ln == 0:
                x = 1

            else:
                x = st[0]
            # out.write(str(x) + " " + str(x) + " " + str(x) + " " + str(x) + "\n")
            t -= 1
            continue

        mn = (4 * (st[0] + st[1]) ** 2) / (st[0] * st[1])
        a, b, c, d = st[1], st[1], st[0], st[0]
        for i in range(1, ln - 1):
            val = (4 * (st[i] + st[i + 1]) ** 2) / (st[i] * st[i + 1])
            if val < mn:
                a, b, c, d = st[i], st[i], st[i + 1], st[i + 1]
                mn = val
        # out.write(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + "\n")
        t -= 1

if __name__ == "__main__":
    main(5)