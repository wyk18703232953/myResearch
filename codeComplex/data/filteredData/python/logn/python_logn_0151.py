import decimal

def main(n):
    # 解释输入结构：
    # 原程序从 input() 读取两个整数 n, k
    # 这里将第一个输入固定为 n（规模），第二个输入 k 由 n 确定性构造
    # 例如令 k = n + 5，保证随规模变化但完全确定
    k = n + 5

    # 以下为原核心逻辑
    coef1 = (k * k - k - 2 * n) * 100 + 225
    if coef1 < 0:
        # print('-1')
        pass

    else:
        D = decimal.Decimal
        coef11 = D(coef1)
        coef1 = coef11.sqrt()
        coef2 = k * 10 - 5
        coef = (coef2 - coef1) / 10
        if coef % 1 == 0:
            # print(int(coef))
            pass

        else:
            # print(int(coef) + 1)
            pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改规模
    main(10)