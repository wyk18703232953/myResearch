import random

def main(n: int):
    # 这里根据 n 生成测试数据（示例：在 [1, n] 范围内随机取一个整数作为原程序的 n）
    test_n = random.randint(1, n)

    # 以下为原始逻辑的封装
    if test_n % 2 == 0:
        print('4 %s' % (test_n - 4))
    else:
        print('9 %s' % (test_n - 9))

# 示例调用
if __name__ == "__main__":
    main(100)