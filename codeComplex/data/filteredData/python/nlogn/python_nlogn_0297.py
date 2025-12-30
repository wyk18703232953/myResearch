from collections import deque
import random

def main(n: int):
    # 生成测试数据：1..n 的随机排列
    orderedli = list(range(1, n + 1))
    random.shuffle(orderedli)

    # 预处理每个值在原排列中的索引（从 1 开始）
    indexof = {}
    for i, x in enumerate(orderedli):
        indexof[x] = i + 1

    # 排序后的数组
    sortedli = sorted(orderedli)

    # 生成长度为 n 的操作序列 s，
    # 保证 0 的总数 = 1 的总数 = n//2（奇数时多一个 0）
    zeros = (n + 1) // 2
    ones = n - zeros
    ops = ["0"] * zeros + ["1"] * ones
    random.shuffle(ops)
    s = "".join(ops)

    st = deque()
    i = 0
    out = []

    for x in s:
        if x == "0":
            st.append(sortedli[i])
            out.append(str(indexof[sortedli[i]]))
            i += 1
        else:  # x == "1"
            temp = st.pop()
            out.append(str(indexof[temp]))

    print(" ".join(out))


if __name__ == "__main__":
    # 示例：n = 10，可按需修改或在外部调用 main(n)
    main(10)