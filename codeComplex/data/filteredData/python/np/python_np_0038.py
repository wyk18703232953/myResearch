import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # s 和 cmd 都为长度 n 的字符串，由 '+', '-' 和 '?' 组成
    choices = ['+', '-', '?']
    s = ''.join(random.choice(choices) for _ in range(n))
    cmd = ''.join(random.choice(choices) for _ in range(n))

    # 原始逻辑
    trgt = 0
    for c in s:
        trgt += (1 if c == '+' else -1)

    queue = [[0, 0]]
    dests = []

    while queue:
        nextqueue = []
        for pos, cmdi in queue:
            if cmdi == len(cmd):
                dests.append(pos)
                continue
            nextcmd = cmd[cmdi]
            if nextcmd == '+':
                nextqueue.append([pos + 1, cmdi + 1])
            elif nextcmd == '-':
                nextqueue.append([pos - 1, cmdi + 1])
            else:
                nextqueue.append([pos + 1, cmdi + 1])
                nextqueue.append([pos - 1, cmdi + 1])
        queue = nextqueue

    occurs = 0
    for x in dests:
        if x == trgt:
            occurs += 1

    print(occurs / len(dests) if dests else 0.0)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)