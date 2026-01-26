import sys

def main(n):
    # 确保 n 为非负整数
    if n < 0:
        raise ValueError("n must be non-negative")
    # 原程序中有 n 个人，每个人的编号出现两次
    # 构造一个确定性的列表 c，长度为 2n
    # 这里采用简单的重复模式：0..n-1 再 0..n-1
    c = list(range(n)) + list(range(n))

    ans = 0
    # 复制一份列表以模拟原程序对列表的破坏性操作
    c = c[:]

    for i in range(n):
        # match the first person
        f = c.pop(0)
        g = c.index(f)
        c.pop(g)
        ans += g

    return ans

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    result = main(10)
    # print(result)
    pass