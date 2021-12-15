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
wonbet_amount = []
win_possitions = []

bet_array = []
print("============== Calculating =================")
for pos,x in enumerate(casino_bet_values):
    
    if x*9 <= max_winning_amount:
        obj = {'bet_value':x,'position':pos+1,'amount':x*9}

        bet_array.append(obj)


def sortbyValue(x):
    return x['bet_value']

bet_array.sort(key=sortbyValue,reverse=True)

cumulative_sum = 0
won_bet_array = []
for x in bet_array:
    if cumulative_sum + x['amount'] <= max_winning_amount:
        cumulative_sum += x['amount']
        print("bet value: ",x['bet_value']," and the position is: ",x['position']," and the amount is: ",x['amount'])
        won_bet_array.append(x)

print("============== Game Summary =================")
print("Owner profit: ",owner_profit)
print("Max Won amt : ",cumulative_sum)
print("Remaning profit amount : ",max_winning_amount - cumulative_sum)


a = [ element["bet_value"] for element in max_winning_amount]
# a =  [x.bet_value for x in max_winning_amount]
print("Won bet arry ",a )
# print('Remaning profit after winning: ',max_winning_amount - sum(wonbet_values))



# Expected Output:
# max won value : 3240
# 250, 100, 10



