def main(n):
    # 生成长度为 n 的只含 '0' 和 '1' 的确定性字符串
    # 规则：第 i 位为 '0' 若 i 为偶数，否则为 '1'
    s = ''.join('0' if i % 2 == 0 else '1' for i in range(n))

    if "0" in s:
        if "1" in s:
            print("1" + "0" * s.count("0"))
        else:
            print("0")
    else:
        print("1")


if __name__ == "__main__":
    main(10)