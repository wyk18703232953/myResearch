from math import sqrt

def main(n):
    # 确定性生成 k，与 n 同规模
    k = n

    answer = int(-1.5 + sqrt(9/4 + 2*(n + k)))
    result = n - answer
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)