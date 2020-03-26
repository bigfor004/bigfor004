class Pokemon:
    def __init__(self, name, weight, height, food, cp):
            self.__name = name  # 選告此方法為私有只能在此類別執行__
            self.__weight = weight
            self.__height = height
            self.__food = food
            self.__cp = cp
    def eat(self):
        print(f'"The pokemon is eating {self.__food}.')

    def make_noise(self):
        print('"The pokemon wow wow wow!')

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_weight(self):
        return self.__weight
    def set_weight(self, new_weight):
        self.__weight = new_weight
    def get_height(self):
        return self.__height
    def set_height(self, new_height):
        self.__height = new_height
    def get_food(self):
        return self.__food
    def set_food(self, new_food):
        self.__food = new_food
    def get_cp(self):
        return self.__cp
    def set_cp(self, new_cp):
        self.__cp = new_cp

class Pikachu(Pokemon):
    def __init__(self, name, weight, height, food, cp):
        super().__init__(self, name, weight, height, food, cp)

    def eat(self):
        print("{self.get_name()} is eating {self.get_food()}. pika")
    def make_noise(self):
        print("{self.get_name()} pika pika chu!")

class Squirtle(Pokemon):
    def __init__(self, name, weight, height, food, cp):
        super().__init__(self, name, weight, height, food, cp)

    def eat(self):
        print("{self.get_name()} is eating {self.get_food()}. jenny jenny")
    def make_noise(self):
        print("{self.get_name()} jenny jenny!")

pokemon = Pokemon('pokemon', 10, 100, '竹竿', 200)

