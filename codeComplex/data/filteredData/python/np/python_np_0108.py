from math import factorial as fact
import random

def main(n: int):
    # 生成测试数据 s 和 t，长度与规模 n 相关
    # 保证 s 中只有 '+' 和 '-'，t 中可以包含 '?'
    # 长度控制在 n 左右，使得 n 为规模控制参数
    length = max(1, n)  # 避免 n 为 0

    # 随机生成 s：仅含 '+' 和 '-'
    choices_s = ['+', '-']
    s = ''.join(random.choice(choices_s) for _ in range(length))

    # 随机生成 t：含 '+', '-', '?'
    choices_t = ['+', '-', '?']
    t = ''.join(random.choice(choices_t) for _ in range(length))

    pos = s.count('+') - t.count('+')
    neg = s.count('-') - t.count('-')
    que = t.count('?')

    if pos < 0 or neg < 0 or pos + neg != que:
        # 注意：原题本意需要 pos + neg == que 才有意义
        print(0)
    else:
        ans = (fact(que) / (fact(pos) * fact(neg))) / (2 ** que)
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)