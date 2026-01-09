import math

def main(n):
    r = n  # 将输入规模 n 同时作为原程序中的 r，保证规模随 n 增长
    if n <= 0:
        return 0.0
    # 为避免 n=1 时出现除零或无意义情况，对 n 小于 2 时做简单处理
    if n < 2:
        n_val = 2

    else:
        n_val = n
    l = 2 * r * math.sin(math.pi / n_val)
    R = l * r / (-l + 2 * r)
    return R

if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    result = main(10)
    # print(result)
    pass