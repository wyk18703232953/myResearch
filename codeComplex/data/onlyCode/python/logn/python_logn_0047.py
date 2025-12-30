import sys
m,n = map(int, sys.stdin.readline().split())  
# 读取两个整数 m 和 n
res = m ^ n                                    
# 异或运算
s = bin(res)                                   
# 转换为二进制字符串 (如 '0b10101')
s = s[2:]                                      
# 去掉 '0b' 前缀，只保留二进制位 (如 '10101')
s = int(s)                                     
# 转换为整数（多余的步骤，不改变值）
if s == 0:
    print(0)                                  
     # 异或结果为0时直接输出0
else:
    s = str(s)                                 
    # 转回字符串
    res = (2 ** len(s)) - 1                    
    # 计算 2^位数 - 1
    print(res)