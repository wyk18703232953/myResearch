def numtostr(a):
    var = []
    while a > 0:
        if a % 26 == 0:
            var.append("Z")
            a = a // 26 - 1
        else:
            var.append(chr(a % 26 - 1 + ord("A")))
            a = a // 26
    var.reverse()
    return "".join(var)


def strtonum(b):
    par = len(b)
    result = 0
    for i in range(1, par):
        result += (26 ** i)
    par = len(b) - 1
    for elem in b:
        if par != 0:
            result += ((ord(elem) - ord("A")) * (26 ** par))
        else:
            result += ((ord(elem) - ord("A")) + 1)

        if par == 0:
            break
        par -= 1
    return result


def method1(par1):
    C = par1.index("C")
    result = numtostr(int(par1[C + 1:])) + par1[1:C]
    return result


def method2(par2):
    c = 0
    for elem in par2:
        try:
            if int(elem):
                break
        except:
            c += 1
    return "R" + par2[c:] + "C" + str(strtonum(par2[:c]))


def generate_test_data(n):
    # 生成 n 条混合格式的测试数据
    data = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            # RC 格式：例如 R23C55
            row = i
            col = i * 3
            data.append(f"R{row}C{col}")
        else:
            # 字母数字格式：例如 BC23
            row = i * 2
            col_letters = numtostr(i)
            data.append(f"{col_letters}{row}")
    return data


def main(n):
    inp = generate_test_data(n)
    for s in inp:
        if "R" in s and "C" in s:
            try:
                if int(s[1:s.index("C")]) and int(s[s.index("C") + 1:]):
                    print(method1(s))
            except:
                print(method2(s))
        else:
            print(method2(s))


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)