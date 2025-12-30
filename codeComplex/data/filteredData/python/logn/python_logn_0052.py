# encontrar o máximo xor entre um par que se encontra no intervalo [l,r]
# 改造说明：
# 1) 去掉 input()
# 2) main(n) 中使用 n 作为区间右端点 r，左端点固定为 0，即求 [0, n] 中任意一对数的最大 xor
# 3) n 即为规模参数，同时作为测试数据规模

def max_xor_in_range(l: int, r: int) -> int:
    if l == r:
        return 0

    l_bin = bin(l)[2:]
    r_bin = bin(r)[2:]

    if len(l_bin) == len(r_bin):
        i = 1  # ambos começam com 1, não preciso checar
        while i < len(l_bin) and l_bin[i] == r_bin[i]:
            i += 1
        tam = len(l_bin) - i
    else:
        tam = len(r_bin)

    num = ""
    for _ in range(tam):
        num += '1'

    return int(num, 2) if num else 0


def main(n: int):
    # 使用 [0, n] 作为区间，根据 n 生成测试数据
    l = 0
    r = n
    ans = max_xor_in_range(l, r)
    print(ans)


# 示例：如需直接运行本文件，可取消以下注释并指定 n
# if __name__ == "__main__":
#     main(10)