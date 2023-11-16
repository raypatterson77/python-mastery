class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.shares)
print(s.price)
print(s.cost())

print('%s %d %.2f' % (s.name, s.shares, s.price))