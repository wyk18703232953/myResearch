import random

def main(n: int):
    # 根据规模 n 生成一个长度为 n 的仅包含 '0' 和 '1' 的随机字符串
    a = ''.join(random.choice('01') for _ in range(n))

    zero = 0
    for ch in a:
        if ch == "0":
            zero += 1

    if "1" in a:
        print("1", end="")
        print("0" * zero)
    else:
        print("0" * zero)


if __name__ == "__main__":
    # 示例：调用 main(10)，需要时可修改规模
    main(10)