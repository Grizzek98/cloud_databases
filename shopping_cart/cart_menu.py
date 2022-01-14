from random import choice
from firebase_admin import firestore

class CartMenu:

    def __init__(self):
        self.db = firestore.client()
        self.current_cart = {}

    def menu_loop(self):
        choice = None
        while choice != 0:
            print('\n---- CART MENU ----')
            print('0) Return to Main Menu')
            print('1) View Cart')
            print('2) Add Item')
            print('3) Remove Item')
            choice = int(input('> '))

            if choice == 1:
                print('\n---- CURRENT CART ----')
                self.view_cart()
            elif choice == 2:
                self.add_item()
            elif choice == 3:
                self.remove_item()
            elif choice != 0:
                print('\nInvalid Choice\n')

    def view_cart(self):
        if self.current_cart:
            for num, item in enumerate(self.current_cart.items(), start=1):
                print(f'{num}) {item[num]} - {item[num-1]}')  
        else:
            print('[Empty]')

    def add_item(self):
        choice = None
        while choice != 0:
            print('\n---- CURRENT CART ----')
            print('0) Return to Previous Menu')
            self.view_cart()


    def remove_item(self):
        choice = None
        while choice != 0:
            print('\n---- CURRENT CART ----')
            print('0) Return to Previous Menu')
            self.view_cart()

            print('Please enter number of item you would like to remove: ')
            