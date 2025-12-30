import random

def main(n: int):
    # 生成规模为 n 的测试数据：随机整数数组 a
    # 这里生成范围可根据需要调整
    a = [random.randint(0, 10**9) for _ in range(n)]

    d = {}
    power = [2**i for i in range(31)]
    ans = []

    for i in a:
        d[i] = 0

    for num in d.keys():
        for p in power:
            if num + p in d:
                ans = [num, num + p]
                if num + p + p in d:
                    print(3)
                    ans.append(num + p + p)
                    print(*ans)
                    return
    if ans:
        print(2)
        print(*ans)
    else:
        print(1)
        print(a[0])


if __name__ == "__main__":
    # 示例调用：可以修改 n 以改变规模
    main(10)