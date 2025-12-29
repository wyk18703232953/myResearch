import random
import string

def main(n: int):
    # 1. 生成规模为 n 的测试字符串，使用小写字母
    #    你也可以根据需要修改生成规则
    s = [random.choice(string.ascii_lowercase) for _ in range(n)]

    # 2. 原逻辑开始
    dic = {}
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            ele = "".join(s[i:j+1])
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1

    ans = []
    for key in dic.keys():
        if dic[key] >= 2:
            ans.append(len(key))
    ans.sort()
    if ans == []:
        print(0)
    else:
        print(ans[-1])


if __name__ == "__main__":
    # 示例：n = 10，可根据需要修改
    main(10)