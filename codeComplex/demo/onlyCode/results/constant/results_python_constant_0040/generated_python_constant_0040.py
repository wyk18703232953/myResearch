# -*- coding: ascii -*-

def main(n: int) -> None:
    # n: problem scale, here directly used as the original n
    lucky = ["1", "2", "3", "5", "6", "8", "9", "0"]

    ye = False
    for i in range(1, n + 1):
        luck = True
        for char in str(i):
            if char in lucky:
                luck = False
                break

        if luck and n % i == 0:
            print("YES")
            ye = True
            break

    if not ye:
        print("NO")


if __name__ == "__main__":
    # 生成测试数据，这里简单使用一个固定的 n 值进行测试
    # 可根据需要调整为任意规模，例如 n = 1000 等
    test_n = 100
    main(test_n)