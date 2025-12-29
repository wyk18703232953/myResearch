import bisect
import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 1~10 的随机整数
    a = [random.randint(1, 10) for _ in range(n)]

    p = [0]
    for x in a:
        p.append(p[-1] + x)

    ans = bisect.bisect_left(p, p[-1] / 2)
    print(ans)


if __name__ == "__main__":
    # 示例：可以根据需要修改 n 的值进行测试
    main(10)