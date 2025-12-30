import random

def main(n):
    # 生成测试数据
    # 保证 k >= 2 且数组元素为正整数
    k = random.randint(2, max(3, n))  # k 在 [2, max(3, n)] 之间
    arr = [random.randint(1, 10 * n) for _ in range(n)]

    # 原逻辑开始
    arr.sort()
    dic = {}
    for a in arr:
        if a / k not in dic:
            dic[a] = 1

    print(len(dic))

if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)