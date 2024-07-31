#Step 1: Build the ItemToPurchase class
class ItemToPurchase:
    def __init__(self, name='none', price=0.0, quantity=0, description='none'):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
    def print_item_cost(self):
        total_cost = self.quantity * self.price
        print(f'{self.name} {self.quantity} @ ${self.price} = ${self.quantity * self.price}')
        return total_cost

# #Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
# items = []
# for i in range(2):
#     print(f'Item {i + 1}')
#     item = ItemToPurchase()
#     item.name = input('Enter the item name:\n')
#     item.price = float(input('Enter the item price:\n'))
#     item.quantity = int(input('Enter the item quantity:\n'))
#     items.append(item)
#     item_cost = item.print_item_cost()
#     i = i + 1
#
# #Step 3: Add the costs of the two items together and output the total cost.
# print('TOTAL COST')
# total_cost = 0
# for item in items:
#     total_cost += item.print_item_cost()
# print(f'Total: ${total_cost}')

#Step 4:Build the ShoppingCart class with the following data attributes and related methods.
# Note: Some can be method stubs (empty methods) initially, to be completed in later steps
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'): #class constructor
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # class attribute

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self,name):
        for item in self.cart_items:
            if item.name == name:
                self.cart_items.remove(item)
                return
        print('Item not found in cart. Nothing Removed')

    def modify_item(self, modified_item):
        found = False
        for item in self.cart_items:
            if item.name == modified_item.name:
                found = True
                if modified_item.price != 0:
                    item.price = modified_item.price
                if modified_item.quantity != 0:
                    item.quantity = modified_item.quantity
                if modified_item.description != 'none':
                    item.description = modified_item.description
                break
        if not found:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num_items = sum(item.quantity for item in self.cart_items)
        return num_items


    def get_cost_of_cart(self):
        total_cost = sum(item.quantity * item.price for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f'{self.customer_name}\'s shopping Cart - {self.current_date}')
        num_items_in_cart = self.get_num_items_in_cart()

        if num_items_in_cart == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print(f'Number of Items: {num_items_in_cart}')
            for item in self.cart_items:
                print(f'{item.name} {item.quantity} @ ${item.price} = ${item.quantity * item.price}')
        total_cost = self.get_cost_of_cart()
        print(f'Total: ${total_cost}')

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print('Item Descriptions:')
        for item in self.cart_items:
            print(f'{item.name}: {item.description}')

#Step 5: In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart parameter
# and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single character. Build and output the menu within the function.
def print_menu(ShoppingCart):
    while True:
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        option = input('Choose an option:').lower()

        if option == 'a': #Step 8 Implement Add item to cart menu option.
            print('ADD ITEM TO CART')
            name = input('Enter the item name:\n')
            description = input('Enter the item description:\n')
            price = float(input('Enter the item price:\n'))
            quantity = int(input('Enter the item quantity:\n'))
            item = ItemToPurchase(name, price, quantity, description)
            ShoppingCart.add_item(item)
        elif option == 'r':    # Step 9: Implement remove item menu option.
            print('REMOVE ITEM FROM CART')
            name = input('Enter name of item to remove:\n')
            ShoppingCart.remove_item(name)
        elif option == 'c': # step 10: Implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem() method.
            print('CHANGE ITEM QUANTITY')
            name = input('Enter the item name:\n')
            quantity = int(input('Enter the new quantity:\n'))
            modified_item = ItemToPurchase(name=name, quantity=quantity)
            ShoppingCart.modify_item(modified_item)
        elif option == 'i':
            ShoppingCart.print_descriptions()
        elif option == 'o':
            ShoppingCart.print_total()
        elif option == 'q':
            print('Thank you for shopping!Have a great day!')
            return
        else:
            print('Invalid option. Please try again.')

#Step 6: Implement Output shopping cart menu option. Implement Output item's description menu option.
# def main():
#     customer_name = input('Enter customer\'s name:\n')
#     current_date = input('Enter today\'s date:\n')
#     shopping_cart = ShoppingCart(customer_name, current_date)
#     print_menu(shopping_cart)

#Step 7:In the main section of your code, prompt the user for a customer's name and today's date.
# Output the name and date. Create an object of type ShoppingCart.
def main():
    customer_name = input('Enter customer\'s name:\n')
    current_date = input('Enter today\'s date:\n')
    print(f'Customer name:{customer_name}')
    print(f'Today\'s date:{current_date}')
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)

if __name__ == '__main__':
    main()
