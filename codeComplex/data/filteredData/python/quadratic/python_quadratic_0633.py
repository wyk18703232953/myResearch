import random

def main(n: int) -> int:
    # 生成测试数据：n 个正整数，范围可按需要调整
    # 这里生成 1 ~ 10**6 内的随机数
    a = [random.randint(1, 10**6) for _ in range(n)]

    a.sort(reverse=True)

    cnt = 0
    while a:
        f = a.pop()
        rm = []
        for x in a:
            if x % f == 0:
                rm.append(x)
        for x in rm:
            a.remove(x)
        cnt += 1

    return cnt


if __name__ == "__main__":
    # 示例：当作脚本运行时，给定一个规模测试
    n = 10
    print(main(n))