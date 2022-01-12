import firebase_admin
from firebase_admin import firestore


class CartMenu:

    def __init__(self):
        self.db = firestore.client()

    def menu_loop(self):
        choice = None
        while choice != 0:
            print('\n---- STORE MENU ----')
            print('1) View Cart')
            print('2) Add Item')
            print('3) Remove Item')
            print('0) Return to Main Menu')
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
        pass

    def add_item(self):
        pass

    def remove_item(self):
        pass