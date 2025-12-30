import random

def main(n: int):
    # 根据规模 n 生成一个长度为 n 的由数字字符组成的字符串，
    # 确保至少有一个非零数字以避免原逻辑中 lower == 0 的退化情况
    if n <= 0:
        return  # 或者按需要改成 print("NO") 等
    digits = [str(random.randint(0, 9)) for _ in range(n)]
    if all(d == '0' for d in digits):
        digits[random.randrange(n)] = str(random.randint(1, 9))
    s = "".join(digits)

    list_n_int = list(map(int, s))

    lower = max(list_n_int)
    total = sum(list_n_int)
    upper = int(total / 2)

    flag = False
    if lower == 0:
        print("YES")
    else:
        for i in range(lower, upper + 1):
            flag = True
            p = 0
            temp = 0
            each = i
            seg = total / each
            if seg.is_integer():
                # 尝试是否可以按 each 为段和划分
                while p < len(s):
                    temp += list_n_int[p]
                    if temp < each:
                        p += 1
                    elif temp == each:
                        temp = 0
                        p += 1
                    else:
                        flag = False
                        break
                if flag:
                    print("YES")
                    break
            else:
                flag = False
        if not flag:
            print("NO")