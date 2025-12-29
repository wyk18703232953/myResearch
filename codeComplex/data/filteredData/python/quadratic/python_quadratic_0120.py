import random

def main(n: int):
    # 生成测试数据：保证 arr 是长度为 n 的整数数组，每个元素在 [1, n] 范围
    # 这里简单生成随机数据，也可按需改成特定分布
    arr = [random.randint(1, n) for _ in range(n)]

    # 原逻辑开始
    for x in range(1, n + 1):
        if x not in arr:
            print(0)
            break
    else:
        print(arr.count(min(arr, key=lambda x: arr.count(x))))

if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)