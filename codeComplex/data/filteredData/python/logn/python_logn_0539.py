def main(n: int):
    # n 视为“第 n 个数字”的查询规模，这里直接用 n 作为原程序的输入
    maxlength = 12

    lengths = [1]
    for i in range(1, maxlength + 1):
        lengths.append(lengths[i - 1] + 9 * i * (10 ** (i - 1)))

    def getnum(k: int) -> int:
        mx = maxlength - 1
        mn = 0
        while True:
            chk = (mx - mn) // 2
            if chk == 0:
                break
            chk += mn
            if k < lengths[chk]:
                mx = chk
            else:
                mn = chk
        curlength = mx
        curlength_ind = k - lengths[curlength - 1]
        curdigind = curlength_ind % curlength
        beforenumscount = curlength_ind // curlength
        result = (
            (beforenumscount // (10 ** (curlength - curdigind - 1))
             + (curdigind == 0)) % 10
        )
        return result

    # 根据 n 生成测试数据：直接用 n 作为要查询的索引
    print(getnum(n))


# 示例：如果需要手动运行，可取消下列注释
# if __name__ == "__main__":
#     main(100)