def main(n):
    # 映射：n -> (no_of_moves, no_of_candy)
    # 为了可规模化，把 no_of_moves 设为 n，no_of_candy 设为 n//2 + 1
    no_of_moves = max(0, n)
    no_of_candy = n // 2 + 1

    total_candy = 1
    now_candy = 1
    now_moves = 1

    if no_of_moves == 0 or (no_of_moves == 1 and no_of_candy == 1):
        # print(0)
        pass
        return

    else:
        while True:
            now_candy = now_candy + 1
            total_candy += now_candy
            now_moves += 1
            if total_candy - (no_of_moves - now_moves) == no_of_candy:
                break

        # print(no_of_moves - now_moves)
        pass
if __name__ == "__main__":
    main(10)