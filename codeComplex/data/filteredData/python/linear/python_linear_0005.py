def main(n):
    # 根据规模 n 生成 n 个测试数据
    # 这里简单生成两种格式交替的测试样例：
    # 奇数行：RxCy 格式，例如 R1C1, R2C2, ...
    # 偶数行：列字母+行数字 格式，例如 A1, B2, ...
    tests = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            # RxCy 格式
            row = i
            col = i
            tests.append(f"R{row}C{col}")
        else:
            # 列字母+行数字 格式
            # 将 i 转为 Excel 列名
            col = i
            v = ''
            while col:
                col -= 1
                r = col % 26
                col //= 26
                v += chr(65 + r)
            tests.append(f"{v[::-1]}{i}")

    # 原逻辑封装，无 input()
    for s in tests:
        ro = co = 0
        for c in s:
            if '0' <= c <= '9':
                ro = 10 * ro + int(c)
            elif ro:
                ro, co = s[1:].split('C')
                ro = int(ro)
                co = int(co)
                v = ''
                while co:
                    co -= 1
                    r = co % 26
                    co //= 26
                    v += chr(65 + r)
                print(v[::-1] + str(ro))
                break
            else:
                co = co * 26 + ord(c) - 64
        else:
            print("R{}C{}".format(ro, co))


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)