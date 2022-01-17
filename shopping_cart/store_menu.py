from shopping_cart.database import Database

class StoreMenu:

    def __init__(self):
        self.db = Database()

    def menu_loop(self):
        choice = None
        while choice != 0:
            print('\n---- STORE MENU ----')
            print('0) Return to Main Menu')
            print('1) Find Items By Category')
            print('2) Add Item to Store')
            print('3) Remove Item from store')
            choice = int(input('> '))

            if choice == 1:
                self.db.view_by_category()
            elif choice == 2:
                self.check_category()
            elif choice != 0:
                print('\nInvalid Choice\n')

    def add_item_to_store(self):
        pass

        
    def check_name(self):
        choice = None
        while choice != 0:
            try:
                print('Please enter name of product:')

            except:
                pass