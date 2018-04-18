import itertools
from item import Item
from validators import validate_credit_card

'''
A shopping cart class for our grocery store program. Keeps track of items, item totals, and grand totals.
Can dislay the cart contents, with subtotals, sorted by subtotal (in ascending or descending order),
alphabetically, or in the order they were added. Also supports checkout with credit card validation,
and can be emptied.
'''

class ShoppingCart:
    new_id = itertools.count(1)
    def __init__(self, items=[]):
        '''
        Sets up an empty shopping cart instance with a unique id.
        '''
        self.items=items
        self.id = next(ShoppingCart.new_id)

    def add_item(self, new_item, quantity):
        '''
        if an item is sold by the store, and there are enough of the item to fulfill the order, this will add the correct
        quantity of the item to the cart. If some number of the item is already present in the cart, it adds to that
        number.
        '''
        if isinstance(new_item, Item):
            if quantity <= new_item.quantity:
                if not new_item in self.items:
                    self.items.append(new_item)
                new_item.quantity -= quantity
                new_item.quantity_in_cart += quantity
                print('{} successfully added to cart.'.format(new_item.name.title()))
                return self.items
            else:
                return 'There are only {} {}s of {} remaining in inventory.'.format(new_item.quantity, new_item.unit, new_item.name)
        else:
            return 'We don\'t sell {}s at this store.'.format(new_item.plural_name)

    def remove_item(self, item):
        if isinstance(item, Item):
            if item in self.items:
                item.quantity += item.quantity_in_cart
                item.quantity_in_cart = 0
                self.items.remove(item)
                print('{} removed from cart.'.format(item.plural_name.title()))
                return self.items
            else:
                print('That item isn\'t in the cart.' )
                return self.items
        else:
            print('That item isn\'t in the cart.' )
            return self.items

    def get_total(self):
        '''
        Returns the grand total cost of the cart's contents.
        '''
        total = 0
        for item in self.items:
            total += item.unit_price * item.quantity_in_cart
        return total/100

    def contents_by_order_added(self):
        '''
        Prints out an itemized list of the items in the cart, ordered by when they were added.
        '''
        for item in self.items:
            print('{}: {} {}s of {}: ${:,.2f}'.format(self.items.index(item)+1, item.quantity_in_cart, item.unit, item.plural_name, item.quantity_in_cart*item.unit_price/100))

    def contents_alphabetically(self):
        '''
        Prints out an itemized list of the items in the cart, ordered alphabetically.
        '''
        items_alphabetically = sorted(self.items, key=lambda x: x.name, reverse=True)
        for item in items_alphabetically:
            print('{}: {} {}s of {}: ${:,.2f}'.format(items_alphabetically.index(item)+1, item.quantity_in_cart, item.unit, item.plural_name, item.quantity_in_cart*item.unit_price/100))
    def contents_by_price(self, direction):
        '''
        Prints out an itemized list of the items in the cart, ordered by subtotal in ascending or descending order.
        '''
        items_by_price = sorted(self.items, key=lambda x: (x.unit_price*x.quantity_in_cart))
        if direction == 'descending':
            for item in items_by_price:
                print('{}: {} {}s of {}: ${:,.2f}'.format(items_by_price.index(item)+1, item.quantity_in_cart, item.unit, item.plural_name, item.quantity_in_cart*item.unit_price/100))
        if direction == 'ascending':
            for item in items_by_price[::-1]:
                print('{}: {} {}s of {}: ${:,.2f}'.format(items_by_price[::-1].index(item)+1, item.quantity_in_cart, item.unit, item.plural_name, item.quantity_in_cart*item.unit_price/100))
    def empty(self):
        '''
        Empties the shopping cart, returning the items to inventory.
        '''
        for item in self.items:
            item.quantity += item.quantity_in_cart
            item.quantity_in_cart = 0
            self.items.remove(item)
        return self.items

    def checkout(self, card_number, name, address):
        '''
        Validates the credit card number and handles user checkout. Prints out a reciept.
        '''
        cc_is_valid = validate_credit_card(card_number)
        if cc_is_valid:
            print('Thanks {}! Your order is on its way!'.format(name))
            print('Reciept:')
            self.empty()
            return True
        else:
            print('That wasn\'t a valid credit card number.')
            return False
