import random

def main(n):
    # 生成测试数据
    # k 在 [1, n] 范围内
    k = random.randint(1, max(1, n))
    # 生成 n 个随机整数，范围可根据需要调整
    arr = [random.randint(1, 10 * n) for _ in range(n)]

    # 原始逻辑
    arr.sort()
    st = []
    for i in arr:
        if not st:
            st.append(i)
        else:
            while st:
                if 0 < abs(st[-1] - i) <= k:
                    st.pop()
                else:
                    break
            st.append(i)
    print(len(st))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)