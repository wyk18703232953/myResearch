import random

def main(n: int) -> int:
    # 根据规模 n 生成测试数据：长度为 n 的只含 '+' 和 '-' 的字符串
    # 这里简单采用等概率随机生成
    random.seed(0)  # 如需每次不同数据，可去掉这一行
    s = ''.join(random.choice('+-') for _ in range(n))

    # 以下为原逻辑的封装与执行
    limit = len(s)
    ans_n = 0

    for i in range(limit + 1):
        flag = True
        stones = i
        for j in s:
            if j == '-':
                if stones > 0:
                    stones -= 1
                else:
                    flag = False
                    break
            else:
                stones += 1

        if flag:
            ans_n = i
            break

    stones = ans_n
    for ch in s:
        if ch == '-':
            stones -= 1
        else:
            stones += 1

    return stones

# 示例：直接运行文件时做一个简单调用
if __name__ == "__main__":
    result = main(10)
    print(result)