class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))
        print('Here are your items: ', end='')
        print(*self.items, sep=', ')

    def add_lemonade(self):
        self.total_cost += 7.5
        self.items += ('lemonade')
        print("Added lemonade!")
    def add_coffee(self):
        self.total_cost += 7.5
        self.items += ('coffee')
        print("Added coffee!")
    def add_fries(self):
        self.total_cost += 7.5
        self.items += ('fries')
        print("Added fries!")
    def add_salad(self):
        self.total_cost += 7.5
        self.items += ('salad')
        print("Added salad!")
   def add_wrap(self):
        self.total_cost += 7.5
        self.items += ('wrap')
        print("Added wrap!")
   def add_steel(self):
        self.total_cost += 7.5
        self.items += ('10 lbs of steel')
        print("Added 10 lbs of steel!")
