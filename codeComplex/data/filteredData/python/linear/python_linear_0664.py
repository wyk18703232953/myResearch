import random

def main(n: int):
    # 生成测试数据
    # l 为长度数组，取 1~10 的随机正整数
    l = [random.randint(1, 10) for _ in range(n)]
    # s 为由 'G', 'W', 'L' 组成的字符串
    # 保证都有可能出现
    choices = ['G', 'W', 'L']
    s = ''.join(random.choice(choices) for _ in range(n))

    water = 0
    grass = 0
    cgrass = 0
    time = 0
    seen = False

    for i in range(n):
        if s[i] == "G":
            dist = l[i]
            if water >= dist:
                water -= dist
                time += 2 * dist
                cgrass += dist
            else:
                dist -= water
                time += 2 * water
                cgrass += water
                water = 0
                time += 3 * dist
                grass += dist
        elif s[i] == "W":
            water += l[i]
            time += 2 * l[i]
            seen = True
        else:
            dist = l[i]
            if water >= dist:
                water -= dist
                time += 2 * dist
            else:
                dist -= water
                time += 2 * water
                water = 0
                if cgrass >= dist:
                    cgrass -= dist
                    grass += dist
                    time += 3 * dist
                else:
                    dist -= cgrass
                    grass += cgrass
                    time += 3 * cgrass
                    cgrass = 0
                    if grass >= dist:
                        grass -= dist
                        time += 3 * dist
                    else:
                        dist -= grass
                        time += 3 * grass
                        grass = 0
                        if seen:
                            time += 4 * dist
                        else:
                            time += 6 * dist

    print(time)
    return time

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)