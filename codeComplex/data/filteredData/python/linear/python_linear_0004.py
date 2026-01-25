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
            result += ((ord(elem) - ord("A")) * ((26) ** par))
        else:
            result += ((ord(elem) - ord("A")) + 1)
        if par == 0:
            break
        par -= 1
    return result

def method1(par1):
    C = par1.index("C")
    result = numtostr(int(par1[C + 1:])) + str(par1[1:C])
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

def generate_inputs(n):
    # 生成两类输入：RC 型和字母数字型，交替排列，规模为 n
    res = []
    # 第一部分：RC 型，如 R1C1, R2C3, ...
    for k in range(1, n + 1):
        row = k
        col = (k * 2) % (n + 5) + 1
        res.append(f"R{row}C{col}")
    # 第二部分：字母数字型，如 A1, B2, ...
    for k in range(1, n + 1):
        col_letters = numtostr((k % 702) + 1)
        row = (k * 3) % (n + 7) + 1
        res.append(f"{col_letters}{row}")
    return res

def main(n):
    inp = generate_inputs(n)
    for key in range(len(inp)):
        if "R" in inp[key] and "C" in inp[key]:
            try:
                if int(inp[key][1:inp[key].index("C")]) and int(inp[key][inp[key].index("C") + 1:]):
                    print(method1(inp[key]))
            except:
                print(method2(inp[key]))
        else:
            print(method2(inp[key]))

if __name__ == "__main__":
    main(10)