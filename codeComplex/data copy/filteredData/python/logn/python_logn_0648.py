def wzor(n):
    return (n * (n + 1)) // 2

def mafia(n, c):
    po = 1
    ko = n
    sr = (po + ko) // 2
    while po != ko:
        if wzor(sr) - (n - sr) >= c:
            ko = sr

        else:
            po = sr + 1
        sr = (po + ko) // 2
    return wzor(po) - c

def main(n):
    # 解释输入规模映射：
    # n 为原问题中的 n
    # 令 c 为一个与 n 同阶的确定性值：c = n // 2
    # 这样时间复杂度主要由 n 控制
    if n < 1:
        return None
    c = n // 2
    result = mafia(n, c)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)