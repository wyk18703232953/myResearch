from math import sqrt, floor, ceil

def main(n: int):
    # 根据规模 n 生成测试数据，这里直接使用 n 自身作为测试参数
    # 若需要批量测试，可在外层循环调用 main 对不同 n 进行测试
    ran = list(range(2, 1 + n // 2))
    xx = [d * (n // d - 1) for d in ran]
    print(sum(xx) * 4)


# 示例调用（根据需要自行修改或在其他模块中调用）
if __name__ == "__main__":
    # 可以在此处指定一个默认规模用于测试
    main(100)