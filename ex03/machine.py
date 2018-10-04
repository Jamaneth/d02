import random
from beverages import *

class CoffeeMachine():

    def __init__(self):
        self.drinks_since_last_repair = 0

    class EmptyCup(HotBeverage):

        def __init__(self):
            self.name = "empty cup"
            self.price = "0.90"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):

        def __init__(self):
            Exception.__init__(self, "This coffee machine has to be repaired.")

    def repair(self):
        self.drinks_since_last_repair = 0

    def serve(self, Beverage):
        if issubclass(Beverage, HotBeverage):
            self.drinks_since_last_repair += 1

            if self.drinks_since_last_repair > 10:
                raise CoffeeMachine.BrokenMachineException()

            else:
                empty_cup_produced = bool(random.randint(0,1))
                if empty_cup_produced:
                    return CoffeeMachine.EmptyCup()

                else:
                    return Beverage()

        else:
            raise Exception("This beverage is not available in this machine.")



if __name__ == '__main__':

    my_machine = CoffeeMachine()
    beverages = [Coffee, HotBeverage, Tea, Cappuccino, Chocolate]

    for beverage_bought in range(0, 22):
        my_beverage = beverages[random.randint(0, 4)]
        try:
            print(my_machine.serve(my_beverage).name)
        except CoffeeMachine.BrokenMachineException:
            print("The coffee machine is broken, so we repair it.")
            my_machine.repair()
