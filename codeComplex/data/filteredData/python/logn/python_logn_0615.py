import random

def candy_eaten(n, k):
    choco = 1
    last = 1
    eat = 0
    i = n - 1
    while i > 0:
        if choco > k:
            temp = choco - k
            choco -= temp
            eat += temp
            i -= temp
        else:
            last += 1
            choco += last
            i -= 1
    return eat

def main(n):
    # 生成测试数据：固定 n，随机生成 k（1 <= k <= 2n，保证有一定变化）
    k = random.randint(1, max(1, 2 * n))
    result = candy_eaten(n, k)
    print(result)

if __name__ == '__main__':
    # 示例：可修改这里的 n 用于本地测试
    main(10)