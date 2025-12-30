import random
import string

def main(n: int):
    # 生成长度为 n 的随机字符串，字符集为小写字母
    cadena = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    # 若希望测试固定字符串，可替换为：
    # cadena = "ababcababc"[:n]

    n = len(cadena)
    rpta = 0

    for i in range(n - 1):
        tamanho_cadena = n - i - 1
        for j in range(n - tamanho_cadena):
            subcadena = cadena[j:j + tamanho_cadena]
            contador = 1
            for k in range(n - tamanho_cadena - j):
                if subcadena == cadena[j + k + 1:j + k + 1 + tamanho_cadena]:
                    contador = contador + 1
            if contador >= 2 and rpta == 0:
                rpta = tamanho_cadena
        if rpta != 0:
            break

    print(rpta)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)