import re

def main(n):
    # 构造一个确定性的字符串，其中包含若干段连续的 'x'
    # 让整体长度与 n 同阶，便于复杂度实验
    parts = []
    for i in range(1, n + 1):
        # 每一段长度是 i % 7 + 1，周期性变化
        run_length = i % 7 + 1
        parts.append('x' * run_length)
        # 在段与段之间插入非 'x' 字符打断
        parts.append('a')
    s = ''.join(parts)

    # 保持原算法逻辑：统计所有长度>=3 的连续 x 段的 (长度 - 2) 之和
    total = sum(len(f) - 2 for f in re.findall('x{3,}', s))
    # print(total)
    pass
    return total

if __name__ == "__main__":
    main(10)