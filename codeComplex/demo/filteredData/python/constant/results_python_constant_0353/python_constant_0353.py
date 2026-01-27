def main(n):
    s = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']
    colors = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
    # 依次从 colors 中取前 min(n, 6) 个颜色作为输入规模
    for idx in range(min(n, len(colors))):
        i = colors[idx]
        if i == 'purple':
            if 'Power' in s:
                s.remove('Power')
        elif i == 'green':
            if 'Time' in s:
                s.remove('Time')
        elif i == 'blue':
            if 'Space' in s:
                s.remove('Space')
        elif i == 'orange':
            if 'Soul' in s:
                s.remove('Soul')
        elif i == 'red':
            if 'Reality' in s:
                s.remove('Reality')
        elif i == 'yellow':
            if 'Mind' in s:
                s.remove('Mind')
    # print(len(s))
    pass
    for stone in s:
        # print(stone)
        pass
if __name__ == "__main__":
    main(4)