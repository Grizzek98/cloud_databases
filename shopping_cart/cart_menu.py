from shopping_cart.database import Database

class CartMenu:

    def __init__(self):
        self.db = Database()
        self.current_cart = []

    def menu_loop(self):
        """ Loops through a list of menu options until a choice is made
        """

        choice = None
        while choice != 0:
            print('\n---- CART MENU ----')
            print('0) Return to Main Menu')
            print('1) View Cart')
            print('2) Add Item')
            print('3) Remove Item')
            choice = int(input('> '))

            if choice == 1:
                self.view_cart()
            elif choice == 2:
                self.add_item()
            elif choice == 3:
                self.remove_item()
            elif choice != 0:
                print('\nInvalid Choice\n')

    def view_cart(self):
        """ Prints the contents of the current cart onto the terminal
        """
        price_list = []
        print("\n---- CURRENT CART ----")
        for num, product in enumerate(self.current_cart, start=1):
            for field in product:
                print (f'{num}) {field:>15}   | ${product[field]:.2f}')
                price_list.append(product[field])
        print('---------------------------')
        print(f'              Total  | ${sum(price_list):.2f}')

    def add_item(self):
        """ Allows the user to add items to the current cart by index
        """

        # return product list by category using Database class
        product_list = self.db.return_product_list()

        # print product list contents
        choice = None
        while choice != 0:
            try:
                print('\n---- ADD ITEM ----')
                print('0) Return')
                for num, doc in enumerate(product_list):
                    print(f'{num+1}) {(doc.to_dict()).get("name")} - ${(doc.to_dict()).get("price"):.2f}')
                try:

                    # receive user input
                    choice = int(input('>'))
                    # add item to cart
                    # TODO could be simplified in the future
                    if choice != 0:
                        product_name = (product_list[choice-1].to_dict())['name']
                        product_price = (product_list[choice-1].to_dict())['price']
                        product_dict = {product_name: product_price}
                        self.current_cart.append(product_dict)
                        choice = None
                except ValueError:
                    print('\nInvalid Choice\n')
                except:
                    print('\nError\n')
            except:
                return

    def remove_item(self):
        """ Allows the user to remove items from the cart by index
        """

        # print cart's contents
        choice = None
        while choice != 0:
            try:
                print('\n---- REMOVE ITEM ----')
                print('0) Return')
                for num, product in enumerate(self.current_cart, start=1):
                    for field in product:
                        print(f'{num}) {field} - ${product[field]:.2f}')

                # receive user input
                choice = int(input('> '))
                if choice !=0:
                    try:
                        # remove item from cart
                        del self.current_cart[choice-1]
                    except:
                        print('Something Happened')
            except ValueError:
                print('\nInvalid Choice\n')