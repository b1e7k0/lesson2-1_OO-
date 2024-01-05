# #     ""'''""""Константы и невидимые переменные, также работа функции def""""""

# DEFAUL_LEVEL_EXPERIENCE = 200

# def is_leveled_up(*, current_expetience: int, gained_experiance: int) -> bool:
#     total_experiance = current_expetience + gained_experiance
#     level_up = False

#     if total_experiance >= DEFAUL_LEVEL_EXPERIENCE:
#         level_up = True
    
#     return level_up

# print(is_leveled_up(current_expetience=150, gained_experiance=60))
# print(is_leveled_up(current_expetience=50, gained_experiance=60)) 


#  """""Использование While"""""""
import random

HEADS = 'heads'
TAILS = 'tails'
COIN_VALUES = [HEADS, TAILS]

def flip_coin():
    return random.choice(COIN_VALUES)

def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_lose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds> 0:
        print('====')
        steps_to_lose += 1
        current_funds -= current_bet
        print(f'{current_funds= }, {current_bet= }')
        fliped_coin_value = flip_coin()
        if fliped_coin_value == HEADS:
            win = current_bet * 2
            print(f'{win= }')
            current_funds += win
            current_bet = min_bet
        else:
            print('loose')
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet =  current_funds
    return steps_to_lose
print(play_martingale(starting_funds=100, min_bet=1, max_bet=100))