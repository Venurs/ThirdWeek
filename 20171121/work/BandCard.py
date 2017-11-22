class BandCard:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_money(self):
        return self.balance

    def set_money(self, money):
        self.balance += money

    def trans(self, money):
        pass

    @classmethod
    def str(cls):
        print(cls.balance, cls.name)


sdg = BandCard("史", 100)
print(sdg.get_money())
sdg.set_money(100)
print(sdg.get_money())
print(str(sdg))
