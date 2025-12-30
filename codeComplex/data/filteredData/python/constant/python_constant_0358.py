def main(n: int):
    # 自动生成 n 个宝石颜色作为测试数据（可根据需要调整）
    colors = ['red', 'purple', 'yellow', 'orange', 'blue', 'green']
    # 若 n 大于 6，就循环使用颜色
    test_inputs = [colors[i % len(colors)] for i in range(n)]

    d = {
        'red': 'Reality',
        'purple': 'Power',
        'yellow': 'Mind',
        'orange': 'Soul',
        'blue': 'Space',
        'green': 'Time'
    }
    stones = ['Reality', 'Power', 'Mind', 'Soul', 'Space', 'Time']

    st = []
    for color in test_inputs:
        st.append(d[color])

    b = []
    for a in stones:
        if a not in st:
            b.append(a)

    print(len(b))
    for k in b:
        print(k)