import random
import string

def main(n: int):
    # 根据 n 生成一个长度为 n 的随机字符串，作为原来 input() 的数据
    # 这里使用小写字母和数字生成
    chars = string.ascii_lowercase + string.digits
    generated_input = ''.join(random.choice(chars) for _ in range(max(n, 0)))
    
    # 保持原程序的输出行为：print(0, 0, input())
    print(0, 0, generated_input)


if __name__ == "__main__":
    # 示例：可修改这里的 n 来做简单测试
    main(10)