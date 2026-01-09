def main(n):
    # 生成确定性字符串 s，长度为 n，元素在 {'0','1','2'} 中循环
    # 映射: i % 3 == 0 -> '0', == 1 -> '1', == 2 -> '2'
    chars = ['0', '1', '2']
    s = ''.join(chars[i % 3] for i in range(n))

    ans = s.replace('1', '') + '2'
    t = ans.find('2')
    result = ans[:t] + '1' * s.count('1') + ans[t:len(ans) - 1]
    # print(result)
    pass
if __name__ == "__main__":
    # 示例规模，可按需修改
    main(10)