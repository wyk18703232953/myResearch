import random
import string

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机小写字符串
    x = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：求字符串中出现至少两次的最长子串长度
    a = 0
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i:j] in x[i+1:]:
                if len(x[i:j]) > a:
                    a = len(x[i:j])
    print(a)


if __name__ == "__main__":
    # 示例：n 可根据需要修改
    main(10)