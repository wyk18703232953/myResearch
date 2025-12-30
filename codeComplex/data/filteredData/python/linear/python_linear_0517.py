import random
import string

def main(n: int) -> int:
    # 生成测试数据：两个长度为 n 的随机小写字母串 a, b
    letters = string.ascii_lowercase
    a = ''.join(random.choice(letters) for _ in range(n))
    b = ''.join(random.choice(letters) for _ in range(n))

    k = True
    result = 0
    z = None  # 原代码中使用到 z，但未初始化，这里显式初始化

    for i in range(n):
        if a[i] == b[i]:
            if k is False:
                result += 1
            k = True
        else:
            if k is False and z != a[i]:
                result += 1
                k = True
            elif k is False and z == a[i]:
                result += 1
            else:
                k = False
                z = a[i]

    if k is False:
        result += 1

    print(result)
    return result

# 示例调用
if __name__ == "__main__":
    main(10)