from math import sqrt, log2
from collections import Counter
import random

def main(n: int):
    # 生成长度为 n 的数字串，避免首位为 '0'
    if n <= 0:
        print(0)
        return

    first_digit = str(random.randint(1, 9))
    if n > 1:
        rest_digits = ''.join(str(random.randint(0, 9)) for _ in range(n - 1))
        num_str = first_digit + rest_digits
    else:
        num_str = first_digit

    ct = 0
    i = 0
    s = []
    while i < len(num_str):
        if not int(num_str[i]) % 3:
            ct += 1
            s.clear()
        else:
            t = int(num_str[i]) % 3
            if 3 - t in s:
                ct += 1
                s.clear()
            else:
                s.append(t)
        if len(s) == 3:
            ct += 1
            s.clear()
        i += 1

    print(ct)


if __name__ == "__main__":
    # 示例：规模 n 可在此修改
    main(20)