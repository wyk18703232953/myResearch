actions, end_total_candies = [int(i) for i in input().split()]
candies = 1
if(actions == 1):
    print(0)
else:
    for i in range(1, actions):
        candies = candies + i + 1
        #print(end_total_candies, candies)
        #print("falta " + str(actions - i - 1) + " acoes")
        if(candies >= end_total_candies + (actions - i - 2)):
            print(candies - end_total_candies)
            exit()
