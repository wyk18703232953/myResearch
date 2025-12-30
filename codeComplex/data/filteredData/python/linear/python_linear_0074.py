import random

def main(n):
    # 生成测试数据：长度为 n 的二进制数组 a、b
    # 可按需要修改生成规则
    a = [random.randint(0, 1) for _ in range(n)]
    b = [random.randint(0, 1) for _ in range(n)]

    b_len = len(b)
    a_len = len(a)

    carCountPrefix = [[0 for _ in range(2)] for _ in range(b_len + 1)]
    b_zero_count = 0
    b_one_count = 0

    for b_i in range(b_len):
        if b[b_i] == 0:
            b_zero_count += 1
        elif b[b_i] == 1:
            b_one_count += 1
        carCountPrefix[b_i + 1][1] = b_one_count
        carCountPrefix[b_i + 1][0] = b_zero_count

    res = 0
    for cur in range(a_len):
        for dig in range(2):
            res += (carCountPrefix[b_len - a_len + cur + 1][dig] - carCountPrefix[cur][dig]) * abs(a[cur] - dig)

    print(res)


if __name__ == '__main__':
    # 示例调用：规模 n 可根据需要修改
    main(5)