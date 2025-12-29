import random

def main(n):
    # 生成测试数据：
    # n: 数组长度
    # k: 比例因子，随机取 1~10
    k = random.randint(1, 10)
    # 生成 n 个随机正整数，范围可根据需要调整
    arr = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑开始
    arr.sort(reverse=True)
    dic = {}
    for a in arr:
        if a * k not in dic:
            dic[a] = 1

    # 返回结果而不是打印，方便在其他地方调用或测试
    return len(dic)

# 示例：当直接运行此文件时，给一个默认规模
if __name__ == "__main__":
    result = main(10)
    print(result)