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
            print('1) Cart Menu')
            print('2) Store Menu')
            print('0) Quit')
            choice = int(input('> '))

            if choice == 1:
                # run the cart menu loop
                self.cart_menu.menu_loop()

            elif choice == 2:
                # run the store menu loop
                self.store_menu.menu_loop()

            elif choice != 0:
                print('\nInvalid Choice\n')