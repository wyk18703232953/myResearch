def is_golden(total, integers):
    current_total = 0
    for i, val in enumerate(integers):
        current_total += val
        if current_total < total:
            continue
        elif current_total == total:
            splice = integers[i + 1:]
            return (not splice) or is_golden(total, splice)
        else:  # current_total > total
            return False
    return False


def solve_ticket(ticket: str) -> str:
    integers = [int(x) for x in ticket]

    zeros = 0
    # count trailing zeros
    while zeros < len(integers) and integers[-1 * (zeros + 1)] == 0:
        zeros += 1

    if zeros > 0 and zeros >= len(integers):
        integers = []
    elif zeros > 0:
        integers = integers[:-1 * zeros]

    if not integers:
        return "YES"
    if len(integers) == 1:
        return "NO"

    total = 0
    for i, val in enumerate(integers[:-1]):
        total += val
        splice = integers[i + 1:]
        if is_golden(total, splice):
            return "YES"
    return "NO"


def main(n: int):
    """
    生成规模为 n 的测试数据并打印判断结果。
    测试数据格式与原程序一致：
      第一行: n
      第二行: 长度为 n 的数字串 ticket
    """
    # 简单的数据生成策略：
    # - 前 n-1 位随机为 0~9，最后一位用来调节使得结果多样
    # 为避免依赖随机模块行为，这里构造一个确定性的 ticket：
    # 规则：循环使用 0..9 直到长度为 n
    if n <= 0:
        return

    digits = []
    base = "0123456789"
    for i in range(n):
        digits.append(base[i % 10])
    ticket = "".join(digits)

    # 打印输入数据
    print(n)
    print(ticket)
    # 打印结果
    print(solve_ticket(ticket))