import random

def start_game_vs_pl(pl1, pl2):
    common_num = 2021
    while common_num > 0:
        print(f'Ходит {pl1}')
        number = int(input(f'На столе {common_num}. {pl1}, cколько конфет возьмете? (не больше 28 и не больше {common_num}): '))
        while number > 28 or common_num - number < 0:
            number = int(input(f'На столе {common_num}. {pl1}, возьми не больше 28 конфет: '))
        common_num -= number
        if common_num == 0:
            print(f'Поздравляем! {pl1} победил!')
        print(f'Ходит {pl2}')
        number = int(input(f'На столе {common_num}. {pl2}, cколько конфет возьмете? (не больше 28): '))
        while number > 28 or common_num - number < 0:
            number = int(input(f'На столе {common_num}. {pl2}, возьми не больше 28 конфет: '))
        common_num -= number
        if common_num == 0:
            print(f'Поздравляем! {pl2} победил!')


def start_game_vs_pl(pl1, pl2):
    common_num = 2021
    while common_num > 0:
        print(f'Ходит {pl1}')
        number = int(input(f'На столе {common_num}. {pl1}, cколько конфет возьмете? (не больше 28 и не больше {common_num}): '))
        while number > 28 or common_num - number < 0:
            number = int(input(f'На столе {common_num}. {pl1}, возьми не больше 28 конфет: '))
        common_num -= number
        if common_num == 0:
            print(f'Поздравляем! {pl1} победил!')
            break
        print(f'Ходит {pl2}')
        number = int(input(f'На столе {common_num}. {pl2}, cколько конфет возьмете? (не больше 28): '))
        while number > 28 or common_num - number < 0:
            number = int(input(f'На столе {common_num}. {pl2}, возьми не больше 28 конфет: '))
        common_num -= number
        if common_num == 0:
            print(f'Поздравляем! {pl2} победил!')
            break

def start_game_vs_cleverbot(hod, pl):
    common_num = 2021
    if hod == '1':
        while common_num > 0:
            print(f'Ходит {pl}')
            number = int(input(f'На столе {common_num}. {pl}, cколько конфет возьмете? (не больше 28 и не больше {common_num}): '))
            while number > 28 or common_num - number < 0 or number <= 0:
                number = int(input(f'На столе {common_num}. {pl}, возьми не больше 28 конфет: '))
            common_num -= number
            if common_num == 0:
                print(f'Поздравляем! {pl} победил!')
                break
            if common_num > 28:
                print(f'Bot взял {29 - number} кофнет.')
                common_num -= 29 - number
            elif common_num < 28:
                print(f'Bot взял последние {common_num} конфет.')
                print('Увы, вы потерпели поражение.')
                break
    else:
        num = 20
        print(f'Bot взял {num} конфет.')
        common_num -= num
        while common_num > 0:
            print(f'Ходит {pl}')
            number = int(input(f'На столе {common_num}. {pl}, cколько конфет возьмете? (не больше 28 и не больше {common_num}): '))
            while number > 28 or common_num - number < 0 or number <= 0:
                number = int(input(f'На столе {common_num}. {pl}, возьми не больше 28 конфет: '))
            common_num -= number
            if common_num == 0:
                print(f'Поздравляем! {pl} победил!')
                break
            if common_num > 28:
                print(f'Bot взял {29 - number} кофнет.')
                common_num -= 29 - number
            elif common_num < 28:
                print(f'Bot взял последние {common_num} конфет.')
                print('Увы, вы потерпели поражение.')
                break


def start_game_vs_stupidbot(hod, pl):
    common_num = 2021
    if hod == 1:
        while common_num > 0:
            print(f'Ходит {pl}')
            number = int(input(f'На столе {common_num}. {pl}, cколько конфет возьмете? (не больше 28 и не больше {common_num}): '))
            while number > 28 or common_num - number < 0 or number <= 0:
                number = int(input(f'На столе {common_num}. {pl}, возьми не больше 28 конфет: '))
            common_num -= number
            if common_num == 0:
                print(f'Поздравляем! {pl} победил!')
                break
            if common_num > 28:
                num = random.randint(1, 28)
                print(f'Bot взял {num} кофнет.')
                common_num -= num
            elif common_num < 28:
                print(f'Bot взял последние {common_num} конфет.')
                print('Увы, вы потерпели поражение.')
                break
    else:
        num = random.randint(1, 28)
        print(f'Bot взял {num} конфет.')
        common_num -= num
        while common_num > 0:
            print(f'Ходит {pl}')
            number = int(input(f'На столе {common_num}. {pl}, cколько конфет возьмете? (не больше 28 и не больше {common_num}): '))
            while number > 28 or common_num - number < 0 or number <= 0:
                number = int(input(f'На столе {common_num}. {pl}, возьми не больше 28 конфет: '))
            common_num -= number
            if common_num == 0:
                print(f'Поздравляем! {pl} победил!')
                break
            if common_num > 28:
                num = random.randint(1, 28)
                print(f'Bot взял {num} кофнет.')
                common_num -= num
            elif common_num < 28:
                print(f'Bot взял последние {common_num} конфет.')
                print('Увы, вы потерпели поражение.')
                break



regim = input('С кем будете играть? 1 - с игроком, 2 - с умным ботом, 3 - с глупым ботом: ')

if regim == '1':
    player1 = input("Имя игрока 1: ")
    player2 = input("Имя игрока 2: ")
    hod = random.randint(1, 2)
    if hod ==1:
        print(f'Первым ходит {player1}')
        start_game_vs_pl(player1, player2)
    else:
        print(f'Первым ходит {player2}')
        start_game_vs_pl(player2, player1)
elif regim == '2':
    player = input("Имя игрока: ")
    hod = random.randint(1, 2)
    if hod == 1:
        print(f'Первым ходит {player}')
        start_game_vs_cleverbot(hod, player)
    else:
        print(f'Первым ходит Bot')
        start_game_vs_cleverbot(hod, player)
else:
    player = input("Имя игрока: ")
    hod = random.randint(1, 2)
    if hod == 1:
        print(f'Первым ходит {player}')
        start_game_vs_stupidbot(hod, player)
    else:
        print(f'Первым ходит {player}')
        start_game_vs_stupidbot(hod, player)