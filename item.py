import itertools

'''
A generic class for grocery store items. Items
'''

class Item:
    new_id = itertools.count(1)
    def __init__(self, name, plural_name, unit_price, unit, quantity=1):
        '''
        Sets up a new item with a unique id, a name, a plural name, a price, a unit of measure, and an optional
        quantity. Quantity in cart defaults to zero, this will be changed when the item is added to a cart.
        '''
        self.id = next(Item.new_id)
        self.name = name
        self.plural_name = plural_name
        self.unit_price = unit_price*100
        self.unit = unit
        self.quantity = quantity
        self.quantity_in_cart = 0
        self.total = self.unit_price * self.quantity

    def add(self, quantity=1):
        self.quantity += quantity
        return self.quantity

    def remove(self, quantity=1):
        if self.quantity - quantity >= 0:
            self.quantity -= quantity
            return self.quantity
        else:
            return 'Can\'t remove that many {}, there are only {} present.'.format(self.plural_name, self.quantity)

    def __str__(self):
        return '{}: ${:,.2f}/{}. In Stock: {}'.format(self.plural_name.title(), self.unit_price/100, self.unit, self.quantity)

if __name__ == '__main__':
    grapefruit = Item('grapefruit', 'grapefruits', 1.99, 'lb', quantity=12)
    print(grapefruit.remove(quantity=50))
