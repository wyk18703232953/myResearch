import random

def main(n):
    # 生成测试数据：n 个随机整数（可根据需要修改生成方式）
    # 例如生成 0 ~ (1<<20)-1 范围内的整数
    test_data = [random.randint(0, (1 << 20) - 1) for _ in range(n)]

    values = []
    idx = []
    # 用于记录每一步的输出结果，便于使用或测试
    outputs = []

    for i in range(n):
        x = test_data[i]
        ans = 0
        for xx, ii in zip(values, idx):
            if (xx ^ x) < x:
                x ^= xx
                ans ^= ii
        if x == 0:
            anss = []
            tmp = ans
            for j in range(i):
                if (tmp & 1) == 1:
                    anss.append(j)
                tmp >>= 1
            # 保持原程序行为：打印
            print(len(anss), *anss)
            outputs.append((len(anss), anss))
        else:
            print(0)
            outputs.append((0, []))
            values.append(x)
            idx.append(ans ^ (1 << i))

    # 返回测试数据和结果，便于调用方验证
    return test_data, outputs

if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)