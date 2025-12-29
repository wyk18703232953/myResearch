import random

def main(n: int):
    # 生成测试数据
    # 约定：n 为数组长度
    # 生成 a,b,c，并保证含义与原程序一致：
    # a: 可用的元素数量上限（不超过 n）
    # b: 目标值
    # c: 初始值
    #
    # 简单策略：
    # - 数组元素在 [1, 10] 内
    # - a 在 [0, n] 内
    # - b, c 在 [0, 10 * n] 内，使得有可能出现可行/不可行两种情况
    
    if n <= 0:
        return  # 无意义规模，直接返回
    
    arr = [random.randint(1, 10) for _ in range(n)]
    a = random.randint(0, n)
    b = random.randint(0, 10 * n)
    c = random.randint(0, 10 * n)

    # 原逻辑开始
    arr.sort()
    p = 0
    a -= 1
    while a >= 0 and c < b:
        c -= 1
        p += 1
        c += arr[a]
        a -= 1

    if c < b:
        print(-1)
    else:
        print(p)


# 示例执行（可注释掉或保留）
if __name__ == "__main__":
    main(10)