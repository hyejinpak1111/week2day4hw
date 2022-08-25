class Items:
    def __init__(self, fish, drink, vegetable):
        self.fish = fish
        self.drink = drink
        self.vegetable = vegetable


class Shopping_cart:

    def __init__(self, fish, drink, vegetable, cart=[]):
        self.fish = fish
        self.drink = drink
        self.vegetable = vegetable
        self.cart = cart

    def add_cart(self, fish, drink, vegetable):
        new_items = Items(fish, drink, vegetable)
        self.cart.append(new_items)


    def print_receipt(self):
        print("=~ *15")
        print("Your Receipt: ")

        for item in self.cart:
            print(item.fish, item.drink, item.vegetable)
    

        print("=~ *15")

    def run(self):
        while True:
            fish = input("What kind of fish do you want for tonight?: ")
            drink = input("What kind of drink do you want?: ")
            vegetable = input("What kind of vegetable do you want to buy?: ")

            self.add_cart (fish, drink, vegetable)
            cont = input("Do you need anything else (y/n)? ")

            if cont == 'n':
                break
        self.print_receipt()

your_cart = Shopping_cart('salmon', 'beer', 'tomato')
your_cart.run()