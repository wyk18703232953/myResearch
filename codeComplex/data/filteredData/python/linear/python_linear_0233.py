from itertools import groupby
import random

def main(n: int) -> int:
    """
    n: 文字列の長さ（規模）
    戻り値: 文字列中に含まれる連続部分文字列 "xxx" の個数
    """
    # 規模 n に応じてテストデータ生成（'x' と 'o' のランダムな文字列）
    s = ''.join(random.choice(['x', 'o']) for _ in range(n))

    # 以降は元コードのロジック
    x_groups = [len(list(group)) for key, group in groupby(s) if key == "x"]
    ans = sum(max(0, l - 3 + 1) for l in x_groups)
    return ans

if __name__ == "__main__":
    # 例: 規模 10 のテスト
    result = main(10)
    print(result)