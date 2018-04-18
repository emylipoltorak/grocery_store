from item import Item
from cart import ShoppingCart
import time

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
    time.sleep(.300)
    print('In Stock Today: ')
    for item in items:
        print(str(item))
    time.sleep(.300)
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
                    time.sleep(.300)
                    continue
            while True:
                try:
                    quantity = float(input('What quantity? '))
                    break
                except ValueError:
                    print('Please enter a number.')
                    continue
            cart.add_item(choice, quantity)
            time.sleep(.700)
            continue

        elif choice == 'b':
            for option in order_options:
                print(option)
            while True:
                try:
                    choice = int(input('How would you like to order the cart contents? Enter the corresponding number: '))
                    if choice > 0 and choice < 5:
                        time.sleep(.300)
                        break
                    else:
                        print('Please enter the number corresponding to your choice. ')
                        time.sleep(.300)
                        continue
                except ValueError:
                    print('Please enter the number corresponding to your choice. ')
                    time.sleep(.300)
                    continue
            if choice == 1:
                cart.contents_by_order_added()
                time.sleep(.700)
            elif choice == 2:
                cart.contents_by_price('ascending')
                time.sleep(.700)
            elif choice == 3:
                cart.contents_by_price('descending')
                time.sleep(.700)
            elif choice == 4:
                cart.contents_alphabetically()
                time.sleep(.700)

        elif choice == 'c':
            print('Your total bill comes to: ${:,.2f}'.format(cart.get_total()))
            time.sleep(.700)

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
                    time.sleep(.300)
                    continue

        elif choice == 'e':
            while True:
                print('I understand that it\'s a bad idea to put a real credit card number into an example app like this. Here\'s an example number that will pass the psuedo credit card validator I wrote: ' )
                time.sleep(.300)
                print('4556 7375 8689 9855')
                time.sleep(.300)
                print('That should work.')
                time.sleep(.300)
                checkout_success = cart.checkout(input('Credit Card Number: '), input('Name on card: ', ), input('Address: '))
                if checkout_success:
                    break
                    time.sleep(.700)
                else:
                    print('Please enter a valid card number. Try our example card number, 4556 7375 8689 9855')
                    time.sleep(.300)
                    continue

        elif choice == 'f':
            cart.empty()
            time.sleep(.300)
            print('Cart has been emptied.')
            time.sleep(.700)


        elif choice == 'q':
            print('Thank you for shopping at Example Mart! Have a nice day!')
            time.sleep(1)
            exit()
        else:
            print('That wasn\'t one of the available options.')
            time.sleep(.700)
            continue


if __name__ == '__main__':
    user_interface()
