import random

def main(n: int) -> int:
    # 生成测试数据：n 个随机正整数，范围可按需要调整
    l = [random.randint(1, 10**6) for _ in range(n)]

    l.sort()
    s = {l[0]}
    res = 1
    for i in l:
        f = 1
        for j in s:
            if i % j == 0:
                f = 0
                break
        if f:
            s.add(i)
            res += 1
    print(res)
    return res

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)