from cities import all_cities
from bot_class import Bot
import random

def button_click():

    allowed_cities = list(all_cities)
    random.shuffle(allowed_cities)

    bot = Bot(allowed_cities.pop()) # Создаём экземляр класса Bot, атрибут которого случайный город из списка

    bot_answer = bot.first_action() # Бот делает первый ход

    # Запускаем цикл 
    game_over = False
    while not game_over:
        user_city = input('Ваша очередь.\n') # Запрашиваем город 

        # Проверяем ответа юзера
        if bot.cheking_user_answer(user_city, bot_answer, \
            allowed_cities, all_cities) == True: # И только в том случае, если всё хорошо, бот делает ход
                                                
            # Цикл для ходов бота
            for possible_city in allowed_cities:
                if possible_city.lower()[0] == user_city[-1]:
                    bot_answer = possible_city
                    bot.playing_process(bot_answer, allowed_cities)
                    break
            
            else:
                bot.lost() 
