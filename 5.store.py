from collections import defaultdict


class Product:
    product_dict = {}

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.product_dict[self.name] = self.price


class User:
    def __init__(self, name, dig=0):
        self.login = name
        self.balance = dig

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if value <= self.__balance:
            self.balance -= value
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')
            return False


class Cart:
    def __init__(self, us):
        self.user = us
        self.goods = defaultdict(int)
        self.__total = 0

    def add(self, pr, value=1):
        if pr.name in self.goods:
            self.goods[pr.name] += value
        else:
            self.goods[pr.name] = value
        self.__total += (pr.price * value)

    def remove(self, pr, value=1):
        if pr.name in self.goods:
            if value == self.goods[pr.name]:
                try_values = value
            elif value > self.goods[pr.name]:
                try_values = self.goods[pr.name]
            else:
                try_values = value
        else:
            return
        if self.goods[pr.name] > value:
            self.goods[pr.name] -= value
        elif self.goods[pr.name] == value:
            self.goods.pop(pr.name)
        else:
            self.goods.pop(pr.name)
        self.__total -= (pr.price * try_values)

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Заказ оплачен')
            self.__total = 0
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for key, value in sorted(self.goods.items(), key=lambda x: x[0]):
            price_per_item = Product.product_dict[key]
            total_price = price_per_item * value
            print(f'{key} {price_per_item} {value} {total_price}')
        print(f'---Total: {self.__total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)
# Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 9)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total)
# 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order()
# Заказ оплачен
print(cart_billy.user.balance)
# 20

print(Product.product_dict)
# {'lemon': 20, 'carrot': 30}