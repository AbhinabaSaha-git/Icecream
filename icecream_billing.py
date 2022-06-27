import math, sys


class Ice_cream:
    total_cost = []
    r_large = 2.5
    r_small = 1.5
    pi = 22.7

    def __init__(self, size):
        self.size = size

    def flavours(self):
        flav = input('please choose your flavour between Vanilla, Chocolate, Butterscotch, Blue_berry: ').lower()
        return flav

    def calculate_cost(self):

        if self.size == 'large':
            vol = 4 / 3 * Ice_cream.pi * Ice_cream.r_large ** 3
            return vol * 0.5
        elif self.size == 'small':
            vol = 4 / 3 * Ice_cream.pi * Ice_cream.r_small ** 3
            return vol * 0.5
        else:
            print("please enter between 'large' or 'small and try again'")
            sys.exit()


class Toppings():

    def choice_of_toppings(self):
        top = input('please enter the choice of toppings available : Hot_fudge, Sprinkles, Caramel, Oreos, Nuts: ')

        topping_list = list(
            filter(lambda a: a == 'Hot_fudge' or a == 'Sprinkles' or a == 'Caramel' or a == 'Oreos' or a == 'Nuts',
                   top.split()))

        return len(topping_list)

    def cost_per_topping(self):
        cost_top = ic_mac.choice_of_toppings() * 2
        return cost_top


class Ice_cream_Machine(Ice_cream, Toppings):

    def __init__(self, size):
        super().__init__(size)

    def icecreamMachine(self):
        print(
            f"your {size} {ic_mac.flavours()} ice cream costs ${round(ic_mac.calculate_cost())}")  # it prints cost of ice cream

        topping_cost = ic_mac.cost_per_topping()

        print(f"your cost of topping is ${topping_cost}")  # it prints topping cost

        #         print(f"your total cost of ice creams is ${topping_cost + round(ic_mac.calculate_cost())}") # it prints total ice cream and topping cost
        Ice_cream.total_cost.append(topping_cost + round(ic_mac.calculate_cost()))


print('"Ice-cream ordereing machine" Welcome to  Ice Cream parlour')

size = input('please enter size of the ice-cream between large or small: ').lower()

ic_mac = Ice_cream_Machine(size)

ic_mac.icecreamMachine()

while True:
    order = input("Do you want to go for another order? ").lower()

    if order == 'yes' or order == 'ya' or order == 'yup':

        size = input('please enter size of the ice-cream between large or small: ').lower()

        ic_mac = Ice_cream_Machine(size)

        ic_mac.icecreamMachine()

    else:
        print('Thank you for ordering from Ice Cream parlour')
        k = 0
        for i in Ice_cream.total_cost:
            k += i
        print(f"your total bill is ${k}")

        break


