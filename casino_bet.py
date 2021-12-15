# casino program

owner_profit_perc = 10
total_win_perc_limit = 90

casino_bet_values = [100,50,500,10,30,700,250,390,880,777]
# casino_bet_values = [1500,1000,500,100,50,10,30,700,250,390,880,777]

sum_of_casino_bet_values = sum(casino_bet_values)
print("Total Bet Values : ",sum_of_casino_bet_values)

max_winning_amount = sum_of_casino_bet_values * total_win_perc_limit / 100
# print("max winning amount: ",max_winning_amount)

owner_profit = sum_of_casino_bet_values * owner_profit_perc / 100
# print("owner profit: ",owner_profit)


print('Max winning amount: ',max_winning_amount)
wonbet_values = []
win_possitions = []
print("============== Calculating =================")
for pos,x in enumerate(casino_bet_values):

    if sum(wonbet_values) <= max_winning_amount:
        won_amt = sum(wonbet_values)+x*9
        if won_amt <= max_winning_amount:
            # print("ie ",won_amt," <= ",max_winning_amount)
            # print("casino bet value is: ",x*9," and the position is: ",pos+1)
            wonbet_values.append(x*9)
            # print("wonbet_values: ",wonbet_values)
            win_possitions.append(pos+1)

print("Winning Possitions : ",win_possitions)
print("Winning Values: ",wonbet_values)

print("============== Game Summary =================")
print("Owner profit: ",owner_profit)
print('Remaning profit after winning: ',max_winning_amount - sum(wonbet_values))


# Result:
# Total Bet Values :  3687
# Max winning amount:  3318.3
# ============== Calculating =================
# Winning Possitions :  [1, 2, 4, 5]
# Winning Values:  [900, 450, 90, 270]
# ============== Game Summary =================
# Owner profit:  368.7
# Remaning profit after winning:  1608.3000000000002

# Expected Output:
# max won value : 3240
# 250, 100, 10

