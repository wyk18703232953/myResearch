def main(n: int):
    # 如果 n == 0，可按需要约定输出，这里沿用原逻辑（0 % i == 0 => YES）
    lucky_divisors = [4, 7, 47, 74, 444, 447, 474, 477, 747, 744, 774, 777]

    for d in lucky_divisors:
        if n % d == 0:
            # print("YES")
            pass
            break

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 根据规模 n 生成测试数据：
    # 这里简单设定为用 n 本身作为待检测数字。
    # 调用时可在此处修改为任何与 n 相关的生成方式。
    test_n = 1000  # 示例规模，可按需更改
    main(test_n)