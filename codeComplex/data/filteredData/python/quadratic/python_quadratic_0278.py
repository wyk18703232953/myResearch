import random

def main(n: int):
    # 生成两个长度为 n 的数组，元素范围 1~n
    m = n  # 原代码中 m 未实质使用，这里令 m = n 以保持对称
    arr1 = [random.randint(1, n) for _ in range(n)]
    arr2 = [random.randint(1, m) for _ in range(m)]

    for first in arr1:
        for second in arr2:
            if first == second:
                print(first, end=" ")


if __name__ == "__main__":
    # 示例：当需要运行测试时，可手动调用 main
    main(5)