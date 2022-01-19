from firebase_admin import firestore
from shopping_cart.cart_menu import CartMenu
from shopping_cart.store_menu import StoreMenu

class MainMenu:

    def __init__(self):
        # establish a connection to the firestore client for the database
        self.db = firestore.client()

        # initialize menu objects
        self.cart_menu = CartMenu()
        self.store_menu = StoreMenu()

    def menu_loop(self):
        """ prints a list of menu options inside of a loop"""
        choice = None
        while choice != 0:
            # print menu options
            print('\n---- MAIN MENU ----')
            print('0) Quit')
            print('1) Cart Menu')
            print('2) Store Menu')
            try:
                choice = int(input('> '))

                if choice == 1:
                    self.cart_menu.menu_loop()
                elif choice == 2:
                    self.store_menu.menu_loop()
                elif choice != 0:
                    print('\nPlease choose an available index')
            except ValueError:
                print('\nInvalid Entry - Choose available index')