import random

def main(n: int) -> int:
    # 生成规模为 n 的测试数据：正整数列表
    # 这里简单生成 1~10^6 之间的随机数，你可按需要修改分布
    if n <= 0:
        return 0
    a = [random.randint(1, 10**6) for _ in range(n)]

    a.sort()
    ans = 0
    while a:
        m = a[0]
        b = []
        for x in a[1:]:
            if x % m != 0:
                b.append(x)
        a = b
        ans += 1
    return ans


if __name__ == "__main__":
    # 示例：运行 main(10) 并打印结果
    print(main(10))