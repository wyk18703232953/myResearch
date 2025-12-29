import random

def main(n: int):
    """
    使用给定规模 n 生成测试数据，并根据原逻辑输出结果。
    这里约定：生成的测试数据为 [1, n] 中的一个随机整数。
    """
    # 根据规模 n 生成测试数据
    if n <= 0:
        # 若规模不合法，默认使用 1
        test_value = 1
    else:
        test_value = random.randint(1, n)

    # 原逻辑开始：判断 test_value 是否为“幸运数”或被幸运数整除
    m = ''.join(set(list(str(test_value))))
    if m == '47' or m == '74' or m == '4' or m == '7':
        print('YES')
    else:
        if (test_value % 4 == 0 or test_value % 7 == 0 or
            test_value % 74 == 0 or test_value % 47 == 0):
            print('YES')
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：调用 main(1000) 作为测试
    main(1000)