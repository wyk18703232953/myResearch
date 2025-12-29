import random

def main(n: int) -> int:
    # 生成测试数据：长度为 n 的列表，元素在 [1, n] 范围内
    daf1 = [random.randint(1, n) for _ in range(n)]

    # 原逻辑开始
    daf2 = {i + 1: 0 for i in range(n)}

    for i in daf1:
        if i in daf2:
            daf2[i] += 1

    result = min(daf2.values())
    print(result)
    return result


if __name__ == "__main__":
    # 示例：手动调用 main，规模 n 可根据需要调整
    main(10)