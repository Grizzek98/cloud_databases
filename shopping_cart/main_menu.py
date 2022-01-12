import firebase_admin
from firebase_admin import firestore
from shopping_cart.cart_menu import CartMenu
from shopping_cart.store_menu import StoreMenu

class MainMenu:

    def __init__(self):
        self.db = firestore.client()
        self.cart_menu = CartMenu()
        self.store_menu = StoreMenu()

    def menu_loop(self):
        choice = None
        while choice != 0:
            print('\n---- MAIN MENU ----')
            print('1) Cart Menu')
            print('2) Store Menu')
            print('0) Quit')
            choice = int(input('> '))

            if choice == 1:
                self.cart_menu.menu_loop()

            elif choice == 2:
                self.store_menu.menu_loop()

            elif choice != 0:
                print('\nInvalid Choice\n')