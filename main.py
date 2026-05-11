import random

# results of player_bot
stats = []
# total plays (make sure it's according to your computing power)
while True :
    try :
        plays_wanted = input("Enter The Number (Times) You Want Let The \
Bots Play (You Can Use Commas ',') : \n")
        no_seprator = int(plays_wanted.replace(',', '_'))
        total_plays = no_seprator
        break
    except ValueError :
        print("Invalid Input, Please Try Again !\n")
        continue
    
def main_game():
    choices = ['r', 'p', 's']
    # total plays (initial)
    plays = 0
    playing = True
    # main loop (continues 100_00 plays)
    while playing:
        # both players' choosed options
        player_bot_choice = random.choice(choices)
        bot_choice = random.choice(choices)
        if plays == total_plays - 1 :
            playing = False
        # Logic for results
        if player_bot_choice == bot_choice:
            stats.append(2)
            plays += 1
            continue
        elif (player_bot_choice == 'r' and bot_choice == 's') or \
             (player_bot_choice == 'p' and bot_choice == 'r') or \
             (player_bot_choice == 's' and bot_choice == 'p'):
            stats.append(1)
            plays += 1
            continue
        else:
            stats.append(0)
            plays += 1
            continue
        

# calculating results
class Results :
    '''calculating draws/wins/loses'''
    def __init__(self, stats):
        self.data = stats
    
    def winings(self) :
        won = stats.count(1)
        return won
    
    def loses(self) :
        lose = stats.count(0)
        return lose
    
    def draws(self) :
        draw = stats.count(2)
        return draw

if total_plays <= 750 :
    tries = 0
    while tries <= 250:    
            main_game()
            winings = Results(stats).winings()/250
            loses = Results(stats).loses()/250
            draws = Results(stats).draws()/250
            tries += 1       
else :
    main_game()
    winings = Results(stats).winings()
    loses = Results(stats).loses()
    draws = Results(stats).draws()
print(f"The following data is based on {plays_wanted} plays of \
Rock, Paper and scissors game between 2 bots : ")
print(f"The Probablity Of Wining Is : {(winings/total_plays)*100}%")
print(f"The Probablity Of Losing Is : {(loses/total_plays)*100}%")
print(f"The Probablity Of Draws Is : {(draws/total_plays)*100}%")

print(f"\n🛑NOTE🛑 : The sum of the data may exceed 100(%), because \
of some binary or calculation(due to small number of attempts) issues.")
