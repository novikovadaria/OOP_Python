class Bot():
    def __init__(self, city):
        self.city = city

    # --- Метод для первого хода
    def first_action(self): 
        print(f'Город {self.city}. Вам на букву - {self.city[-1]}\n')
        return self.city

    # --- Метод для проверки ответа игрока
    def cheking_user_answer(self, user_city, bot_answer, \
        allowed_cities, all_cities): 
        
        if user_city.lower()[0] != bot_answer[-1]:
            print(f"Неверно, город должен начинатся с буквы {bot_answer[-1]}")
            return False

        elif user_city not in all_cities:
            print("Такого города нет в России, повторите попытку.\n")
            return False

        elif user_city not in allowed_cities:
            print("Этот город уже был.")
            return False
        
        else:
            print(f"Верно! Мне на букву {user_city[-1]}")
            allowed_cities.remove(user_city)
            return True

    # --- Метод для хода бота
    def playing_process(self, bot_answer, allowed_cities):
            allowed_cities.remove(bot_answer)
            print(f"Мой ответ - {bot_answer}. Вам на букву {bot_answer[-1]}")

    # --- Метод для вывода сообщения о победе игрока
    def lost(self):
        print(f'Вы победили!')

    
    


