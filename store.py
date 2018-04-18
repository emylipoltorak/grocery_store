from item import Item
from cart import ShoppingCart

cart = ShoppingCart()

apple = Item('apple', 'apples', 1.99, 'lb', quantity=50)
bread = Item('bread', 'bread', 4.75, 'loaf', quantity=287)
milk = Item('milk', 'milk', 2.00, 'gallon', quantity=43)
chips = Item('chips', 'chips', 3.50, 'bag', quantity=68)

items = [apple, bread, milk, chips]
options = ['A: Add item to cart',
'B: Display cart contents',
'C: Calculate total cost',
'D: Remove item from cart',
'E: Check out',
'F: Empty cart',
'Q: Quit']
order_options = [
'1: Order by order added',
'2: Order by price (ascending)',
'3: Order by price (descending)',
'4: Order alphabetically'
]

def user_interface():
    print('Welcome To Example Mart!')
    print('In Stock Today: ')
    for item in items:
        print(str(item))
    while True:
        print('What would you like to do?')
        for option in options:
            print(option)
        choice = input('Enter the corresponding letter: ').lower()
        if choice == 'a':
            for item in items:
                print('{}: {}'.format(items.index(item)+1, str(item)))
            while True:
                try:
                    choice = items[int(input('What would you like to buy? Enter the number corresponding to the item: '))-1]
                    print(choice)
                    break
                except:
                    print('That\'s not an item we sell.')
                    continue
            while True:
                try:
                    quantity = float(input('What quantity? '))
                    break
                except ValueError:
                    print('Please enter a number.')
                    continue
            cart.add_item(choice, quantity)
            continue

        elif choice == 'b':
            for option in order_options:
                print(option)
            while True:
                try:
                    choice = int(input('How would you like to order the cart contents? Enter the corresponding number: '))
                    if choice > 0 and choice < 5:
                        break
                    else:
                        print('Please enter the number corresponding to your choice. ')
                        continue
                except ValueError:
                    print('Please enter the number corresponding to your choice. ')
                    continue
            if choice == 1:
                cart.contents_by_order_added()
            elif choice == 2:
                cart.contents_by_price('ascending')
            elif choice == 3:
                cart.contents_by_price('descending')
            elif choice == 4:
                cart.contents_alphabetically()

        elif choice == 'c':
            print('Your total bill comes to: ${:,.2f}'.format(cart.get_total()))

        elif choice == 'd':
            for item in cart.items:
                print('{}: {}'.format(cart.items.index(item)+1, item.name))
            while True:
                try:
                    choice = items[int(input('What would you like to remove from your cart? Enter the number corresponding to the item: '))-1]
                    cart.remove_item(choice)
                    break
                except:
                    print('Please enter a valid selection.')
                    continue

        elif choice == 'e':
            while True:
                print('I understand that it\'s a bad idea to put a real credit card number into an example app like this. Here\'s an example number that will pass the psuedo credit card validator I wrote: ' )
                print('4556 7375 8689 9855')
                print('That should work.')
                checkout_success = cart.checkout(input('Credit Card Number: '), input('Name on card: ', ), input('Address: '))
                if checkout_success:
                    break
                else:
                    print('Please enter a valid card number. Try our example card number, 4556 7375 8689 9855')
                    continue

        elif choice == 'f':
            cart.empty()
            print('Cart has been emptied.')
            continue

        elif choice == 'q':
            print('Thank you for shopping at Example Mart! Have a nice day!')
            exit()
        else:
            print('That wasn\'t one of the available options.')
            continue


if __name__ == '__main__':
    user_interface()
