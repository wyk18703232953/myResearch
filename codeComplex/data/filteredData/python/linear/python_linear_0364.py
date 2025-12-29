import random

def main(n):
    # 生成测试数据
    # n 表示数组 a 的长度
    # m 随机设定为 [0, n] 区间内的整数
    m = random.randint(0, n)
    a = [random.randint(1, 100) for _ in range(n)]
    b = [random.randint(1, 100) for _ in range(m)]

    # 为了更符合原题常见场景（如匹配问题），可以排序 b
    b.sort()

    ans = 0
    # 复制 b，避免后续如需复用原测试数据结构
    bb = b[:]
    for i in range(len(a)):
        if len(bb) == 0:
            break
        if bb[0] >= a[i]:
            ans += 1
            del bb[0]

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模 n = 10
    main(10)