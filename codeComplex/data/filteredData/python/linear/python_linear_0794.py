def main(n):
    # Generate n tile strings deterministically.
    # Each tile is like "1m", "2p", "3s" etc.
    suits = "mps"
    tiles = []
    for i in range(n):
        number = i % 9 + 1  # 1..9
        suit = suits[(i // 9) % 3]
        tiles.append(str(number) + suit)

    a = tiles
    st = set([])
    cnt = [[0 for _ in range(9)] for _ in range(3)]
    for e in a:
        cnt['mps'.index(e[1])][int(e[0]) - 1] = 1
        st.add(e)
    answ = len(st) - 1
    for i in range(3):
        for j in range(7):
            answ = min(answ, 3 - sum(cnt[i][j:j + 3]))
    # print(answ)
    pass
if __name__ == "__main__":
    main(14)