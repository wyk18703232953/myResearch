import random

def main(n):
    # 生成测试数据
    # a、b 均为长度为 n 的数组，元素范围在 1~2n
    m = n  # 原代码中 m 未被实际使用，这里设为与 n 相同
    a = [random.randint(1, 2 * n) for _ in range(n)]
    b = [random.randint(1, 2 * n) for _ in range(m)]

    # 原逻辑：输出在 b 中出现过的 a 中元素
    for i in a:
        if i in b:
            print(i, end=' ')

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)