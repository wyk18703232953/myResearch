import random

def main(n: int):
    # 生成规模为 n 的测试数据：在区间 [0, n] 中随机取两个数 l, r
    l = random.randint(0, n)
    r = random.randint(0, n)
    if l > r:
        l, r = r, l

    ans = l ^ r
    j = 0
    while (1 << j) <= ans:
        ans |= (1 << j)
        j += 1

    print(ans)

if __name__ == "__main__":
    # 示例：将规模设置为 10
    main(10)