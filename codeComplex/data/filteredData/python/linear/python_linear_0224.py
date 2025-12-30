import random

def main(n: int):
    # 根据 n 生成测试数据：长度为 n 的只含 '0' 和 '1' 的字符串
    s = ''.join(random.choice('01') for _ in range(n))

    if "0" in s:
        if "1" in s:
            print("1" + "0" * s.count("0"))
        else:
            print("0")
    else:
        print("1")


if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(10)