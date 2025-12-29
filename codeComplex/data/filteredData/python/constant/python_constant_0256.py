import random

def main(n):
    # 生成测试数据：
    # n 为整体规模
    # pos 在 [1, n]
    # l, r 满足 1 <= l <= r <= n
    pos = random.randint(1, n)
    l = random.randint(1, n)
    r = random.randint(l, n)

    if l == 1 and r == n:
        result = 0
    elif l == 1 and r != n:
        result = abs(pos - r) + 1
    elif l != 1 and r == n:
        result = abs(pos - l) + 1
    else:
        result = r - l + 2 + min(abs(pos - l), abs(pos - r))

    print(result)

if __name__ == "__main__":
    # 示例调用，默认规模为 10，可按需修改
    main(10)