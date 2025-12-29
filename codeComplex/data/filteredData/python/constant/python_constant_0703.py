import random

def main(n):
    # 生成测试数据：根据规模 n 生成 citys, cap
    # 这里简单设置 citys = n，cap 在 [1, n] 随机生成
    citys = n
    cap = random.randint(1, max(1, n))  # 避免 n 为 0 时出错

    if citys - 1 <= cap:
        result = citys - 1
    else:
        diff = citys - cap
        result = diff * (diff + 1) // 2 + cap - 1

    print(result)


if __name__ == "__main__":
    # 示例：可修改为任意规模
    main(10)