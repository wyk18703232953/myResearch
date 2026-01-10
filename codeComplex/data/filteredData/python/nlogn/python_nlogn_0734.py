import math

def main(n):
    # 映射含义：
    # n -> m（元素个数），k 固定为 10，n 固定为 m * 2
    # 构造一个递增的 p 数组，满足原逻辑的需求
    m = max(1, n)
    k = 10
    total_pages = m * 2
    # 构造 p：前一半较密集，后一半间隔更大
    p = []
    for i in range(m):
        if i < m // 2:
            p.append(i + 1)
        else:
            p.append(total_pages - (m - i - 1) * 2)
    p.sort()
    page_max = k
    action_count = 0
    index = 0
    while index < m:
        while index < m and p[index] <= page_max:
            count = 0
            while index < m and p[index] <= page_max:
                index += 1
                count += 1
            if count > 0:
                action_count += 1
            page_max += count

        pc = 1 if index >= m else math.ceil((p[index] - page_max) / k)
        page_max += k * pc

    return action_count

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做实验
    print(main(1000))