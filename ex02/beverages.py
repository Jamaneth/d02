# -*- coding: utf-8 -*-

class HotBeverage():

    def __init__(self):
        self.price = "0.30"
        self.name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return "name : " + self.name + "\nprice : " + self.price + "\ndescription : " + self.description()


class Coffee(HotBeverage):

    def __init__(self):
        self.price = "0.40"
        self.name = "coffee"

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):

    def __init__(self):
        super().__init__()
        self.name = "tea"

class Chocolate(HotBeverage):

    def __init__(self):
        self.name = "chocolate"
        self.price = "0.50"

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):

    def __init__(self):
        self.name = "cappuccino"
        self.price = "0.45"

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__ == '__main__':

    hotbeverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    for beverage in [hotbeverage, coffee, tea, chocolate, cappuccino]:
        print(beverage)
