import sys

def generate_input(n):
    # 第一行：占位（原代码中被丢弃）
    # 第二行：n 个互不相同的整数，构成一个排列结构
    # 使用确定性的构造方式，无随机
    if n <= 0:
        n = 1
    arr = [(i * 2 + 3) % n for i in range(n)]
    # 为保证是排列且元素从 0..n-1 打乱后再平移到 1..n
    seen = set()
    perm = []
    for v in arr:
        if v not in seen:
            seen.add(v)
            perm.append(v)
    # 补齐缺失的元素
    for v in range(n):
        if v not in seen:
            perm.append(v)
    # 现在 perm 是 0..n-1 的排列，将其平移到 1..n
    perm = [v + 1 for v in perm[:n]]
    # 构造模拟输入（第一行随意，第二行为排列）
    lines = []
    lines.append(str(n))
    lines.append(" ".join(str(x) for x in perm))
    return lines

def main(n):
    lines = generate_input(n)
    it = iter(lines)

    # 丢弃第一行
    next(it)

    positions = {}
    pos2x = {}
    for i, x in enumerate(next(it).split()):
        x = int(x)
        positions[x] = i
        pos2x[i] = x

    answers = ['' for _ in range(len(positions))]

    for x in range(len(positions), 0, -1):

        position = positions[x]

        def can_go_to_looser():
            next_position = position + x
            while next_position < len(positions):
                if pos2x[next_position] > x and answers[next_position] == "B":
                    return True
                next_position += x

            next_position = position - x
            while next_position >= 0:
                if pos2x[next_position] > x and answers[next_position] == "B":
                    return True
                next_position -= x

            return False

        if can_go_to_looser():
            answers[position] = "A"
        else:
            answers[position] = "B"

    result = ''.join(answers)
    print(result)
    return result

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值做规模实验
    main(10)