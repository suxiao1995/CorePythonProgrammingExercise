# -*- coding: utf-8 -*-
__author__ = 'lihui'


#13-11
class User(object):
    def __init__(self):
        self.cart = Cart()
        self.item = Item()

    def buy(self):
        self.item.show()
        item_name = int(raw_input("Enter the name:"))
        num = int(raw_input("Enter numbers:"))
        self.item.sold(item_name, num)
        self.cart.add(item_name, num)


    def check_cart(self):
        self.cart.show()

    def cancel(self):
        self.cart.show()
        item_name = int(raw_input("Enter the name:"))
        num = int(raw_input("Enter numbers:"))
        self.cart.delete(item_name, num)

class Item(dict):

    def show(self):
        for key in self:
            print key,":",self[key]

    def sold(self, item_name, num):
        print "Sold %d item" % num
        if self.is_empty() == True:
            print "Storehouse is empty!"
        if self[item_name] < num:
            print "Only %d left!" % self[item_name]
        else:
            self[item_name] -= num


    def is_empty(self):
        return len(self) == 0

class Cart(dict):

    def show(self):
        for key in self:
            print key,":",self[key]

    def delete(self, item_name, num):
        if self.is_empty() == True:
            print "Your cart is empty!"

        self[item_name] -= num
        print " %d left!" % self[item_name]
        if self[item_name] <= 0:
            del self[item_name]


    def add(self, goods, num):
        if goods not in self:
            self[goods] = num
        else:
            self[goods] += num

    def is_empty(self):
        return len(self) == 0


