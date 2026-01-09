def main(n):
    # 映射：n 作为右端点 r，左端点 l = 0
    # 保持原算法逻辑不变
    l = 0
    r = n
    diff = (r ^ l)
    result = pow(2, diff.bit_length()) - 1
    # print(result)
    pass
if __name__ == "__main__":
    main(10)