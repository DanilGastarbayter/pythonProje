import random
class Human:
    def __init__(self, name = "maynkrafter3000", job = None, home = None, car = None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        pass
    def get_job(self):
        pass
    def get_car(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def get_shopping(self):
        pass
    def chill(self):
        pass
    def clear_home(self):
        pass
    def day_indexes(self, day):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']
brands_of_cars = {'тумбочка': {'fuel':2, 'strength'1, 'consumption':1}}, {'ракета': {'fuel':100, 'strength'100000000, 'consumption':100}}, {'тумбочка x bmv': {'fuel':1, 'strength'10000000000000000, 'consumption':0}}