import random

def main(n):
    # n 将作为 t 的规模：生成 t = n 个元素的升序数组
    t = n

    # 随机生成 d，避免 d = 0 的情况
    d = random.randint(1, 10)

    # 生成一个严格递增的数组 arr，长度为 t
    # 使用随机步长，确保递增
    arr = []
    current_val = 0
    for _ in range(t):
        step = random.randint(1, 10)
        current_val += step
        arr.append(current_val)

    # 原始逻辑
    count = 0
    for i in range(t - 1):
        diff = arr[i + 1] - arr[i]
        if diff == 2 * d:
            count += 1
        elif diff > 2 * d:
            count += 2

    result = count + 2

    # 返回结果与生成的数据，方便调试或验证
    return {
        "t": t,
        "d": d,
        "arr": arr,
        "result": result
    }

# 示例调用（实际使用时可删除或注释）
if __name__ == "__main__":
    output = main(5)
    print(output["result"])