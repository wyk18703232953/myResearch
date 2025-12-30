import random

def main(n):
    # 生成测试数据：n 个整数，以及 k
    # 可根据需要调整数据范围
    k = random.randint(0, 10)
    arr = [random.randint(0, 100) for _ in range(n)]

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
    # 示例：调用 main，规模可自行调整
    main(10)