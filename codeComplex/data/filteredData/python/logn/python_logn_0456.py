import random

def judge(a, b, secret_a, secret_b):
    """
    模拟交互器：
    返回 sign( (secret_a ^ a) - (secret_b ^ b) )
    """
    va = secret_a ^ a
    vb = secret_b ^ b
    if va < vb:
        return -1
    elif va > vb:
        return 1
    else:
        return 0

def main(n):
    """
    n 作为规模参数，用于控制生成 secret_a, secret_b 的范围：
    0 <= secret_a, secret_b < 2^min(n, 30)
    """
    max_bits = min(n, 30)
    limit = 1 << max_bits

    # 生成测试数据
    secret_a = random.randrange(limit)
    secret_b = random.randrange(limit)

    # 模拟原始交互逻辑
    cond = judge(0, 0, secret_a, secret_b)
    cur_a = 0
    cur_b = 0

    for i in range(29, -1, -1):
        xor = (1 << i)
        query_a = cur_a ^ xor
        query_b = cur_b ^ xor
        val = judge(query_a, query_b, secret_a, secret_b)

        if val != cond:
            if cond == -1 and val == 1:
                cur_b ^= xor
                query_a = cur_a
                query_b = cur_b
                val = judge(query_a, query_b, secret_a, secret_b)
                cond = val
            else:
                cur_a ^= xor
                query_a = cur_a
                query_b = cur_b
                val = judge(query_a, query_b, secret_a, secret_b)
                cond = val
        else:
            cond = val
            query_a = cur_a ^ xor
            query_b = cur_b
            val = judge(query_a, query_b, secret_a, secret_b)
            if val == -1:
                cur_a ^= xor
                cur_b ^= xor
            else:
                pass

    # 输出推断结果与真实答案，便于验证
    print("guessed_a =", cur_a, "guessed_b =", cur_b)
    print("secret_a  =", secret_a, "secret_b  =", secret_b)
    print("correct   =", (cur_a == secret_a and cur_b == secret_b))

if __name__ == "__main__":
    # 示例: 调用 main(30)，可根据需要修改 n
    main(30)