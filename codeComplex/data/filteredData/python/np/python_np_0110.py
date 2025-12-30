import math
import random

def main(n):
    # 1. 根据规模 n 生成测试数据
    # 让 send 串含有 n 个字符，每个字符为 '+' 或 '-'
    # rcv 串为对 send 的一个随机子集的打乱（保证 flag=1 的情况）
    send_list = [random.choice(['+', '-']) for _ in range(n)]
    send = ''.join(send_list)

    # 随机选择 rcv 的长度在 [0, n]，并从 send 中选取该长度的随机子集
    rcv_len = random.randint(0, n)
    indices = random.sample(range(n), rcv_len)
    rcv_list = [send_list[i] for i in indices]
    random.shuffle(rcv_list)
    rcv = ''.join(rcv_list)

    # 2. 原逻辑开始（去掉 input，改用生成的 send, rcv）
    d = {'+': 0, '-': 0}
    for ch in send:
        d[ch] += 1

    flag = 1
    for ch in rcv:
        if ch in d:
            if d[ch] == 0:
                flag = 0
            else:
                d[ch] -= 1

    tot = d['+'] + d['-']
    totComb = 2 ** tot
    n_val = tot
    r_val = d['+']

    # 若 tot 为 0，防止 0! 的边界问题，但原逻辑数学上仍然成立
    npr = math.factorial(n_val) / math.factorial(n_val - r_val) if n_val >= r_val else 0
    reqComb = npr / math.factorial(r_val) if r_val >= 0 else 0

    if flag == 0:
        print('0.00000000')
    else:
        print(float(reqComb) / totComb)


# 示例：调用 main(10) 或其他规模
if __name__ == "__main__":
    main(10)