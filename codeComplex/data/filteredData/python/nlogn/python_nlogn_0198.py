import random

def almost_difference(array):
    n = len(array)
    if n == 1:
        return 0

    dict_equal = dict()
    ad_sum = 0
    prev_sum = 0

    for i in range(n):
        x = array[i]
        if x not in dict_equal:
            dict_equal[x] = 0
        if x - 1 not in dict_equal:
            dict_equal[x - 1] = 0
        if x + 1 not in dict_equal:
            dict_equal[x + 1] = 0

        ad_sum = ad_sum + i * x - prev_sum + dict_equal[x + 1] - dict_equal[x - 1]
        dict_equal[x] += 1
        prev_sum += x

    return ad_sum


def generate_test_data(n):
    # 生成规模为 n 的测试数据，元素范围可根据需要调整
    # 这里选取较小范围便于调试与验证
    return [random.randint(1, 10**6) for _ in range(n)]


def main(n):
    array = generate_test_data(n)
    result = almost_difference(array)
    print(result)


if __name__ == "__main__":
    # 示例：运行时可自行修改 n
    main(5)