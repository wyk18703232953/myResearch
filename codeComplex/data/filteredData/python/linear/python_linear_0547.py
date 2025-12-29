import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组 a，元素为 0~n 之间的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    mex = -1
    for i in range(n):
        if a[i] <= mex:
            continue
        elif a[i] == mex + 1:
            mex += 1
        else:
            print(i + 1)
            return
    print(-1)


if __name__ == "__main__":
    # 示例：运行规模 n=10 的测试
    main(10)