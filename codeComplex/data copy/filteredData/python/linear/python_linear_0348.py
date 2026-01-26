import math

def main(n):
    # 确定性生成 k 和区间 [l, r]
    # 这里让 k 与 n 线性相关，便于规模化实验
    k = max(1, n // 2)
    queries = []
    for idx in range(k):
        # 生成一组确定性的区间 [l, r]
        # 使用简单算术从 n 和 idx 推导
        l = (idx * 2) % max(1, n) + 1
        r = (idx * 3) % max(1, n) + 1
        if l > r:
            l, r = r, l
        queries.append((l, r))
    # 原始程序对读入的区间不做任何处理，因此这里只是生成但不使用

    # 保持原来的核心输出逻辑：长度为 n 的 1010... 序列
    for i in range(1, n + 1):
        if i % 2 == 0:
            # print('0', end='')
            pass

        else:
            # print('1', end='')
            pass
    # print()
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(10)