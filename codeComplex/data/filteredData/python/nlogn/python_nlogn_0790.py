import random

def main(n):
    # 1. 生成测试数据
    # 随机生成 1 <= k <= n
    k = random.randint(1, n)
    # 生成长度为 n 的数组 arr，这里生成非降序数组以保证差值非负（可按需调整）
    arr = sorted(random.randint(0, 1000) for _ in range(n))

    # 2. 原程序逻辑
    new_arr = []
    for i in range(n - 1):
        new_arr.append(arr[i + 1] - arr[i])

    new_arr.sort()
    result = sum(new_arr[:n - k])

    # 返回结果与用于调试的测试数据
    return {
        "n": n,
        "k": k,
        "arr": arr,
        "result": result
    }

# 示例调用
if __name__ == "__main__":
    info = main(10)
    print("n =", info["n"])
    print("k =", info["k"])
    print("arr =", info["arr"])
    print("result =", info["result"])