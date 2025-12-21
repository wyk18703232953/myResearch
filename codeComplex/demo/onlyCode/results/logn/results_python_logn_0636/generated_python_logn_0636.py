def main(n):
    actions = n
    end_total_candies = n * (n + 1) // 2
    candies = 1
    if actions == 1:
        return 0
    else:
        for i in range(1, actions):
            candies = candies + i + 1
            if candies >= end_total_candies + (actions - i - 2):
                return candies - end_total_candies

if __name__ == "__main__":
    print(main(10))