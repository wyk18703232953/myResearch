import math
import random

def main(n: int):
    # 生成目标串 inp：长度为 n，只含 '+' 和 '-'
    inp = ''.join(random.choice('+-') for _ in range(n))

    # 生成猜测串 dec：长度也为 n，含 '+', '-', '?'
    # 这里的策略：随机在 '+', '-', '?' 中选择
    dec = ''.join(random.choice('+-?') for _ in range(n))

    inp_dict = {"+": 0, "-": 0}
    dec_dict = {"+": 0, "-": 0, "?": 0}

    for ch in inp:
        if ch == "+":
            inp_dict["+"] += 1
        elif ch == "-":
            inp_dict["-"] += 1

    for ch in dec:
        if ch == "+":
            dec_dict["+"], = (dec_dict["+"] + 1,)
        elif ch == "-":
            dec_dict["-"] += 1
        elif ch == "?":
            dec_dict["?"] += 1

    if dec_dict["+"] == inp_dict["+"] and dec_dict["-"] == inp_dict["-"]:
        print(f"{1.0000000000:.10f}")
    else:
        temp = inp_dict["+"] - dec_dict["+"]
        temp1 = inp_dict["-"] - dec_dict["-"]

        if temp + temp1 == dec_dict["?"] and temp >= 0 and temp1 >= 0:
            total = temp + temp1
            # 计算组合数 C(total, temp) * (1/2)^(total)
            comb = math.factorial(total) / (math.factorial(temp) * math.factorial(temp1))
            prob = comb * (0.5 ** total)
            print(f"{prob:.10f}")
        else:
            print(f"{0.0000000000:.10f}")

if __name__ == "__main__":
    # 示例：n = 10，可根据需要修改或由外部调用 main(n)
    main(10)