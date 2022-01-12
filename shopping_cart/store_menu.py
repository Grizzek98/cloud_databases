import firebase_admin
from firebase_admin import firestore


class StoreMenu:

    def __init__(self):
        self.db = firestore.client()

    def menu_loop(self):
        choice = None
        while choice != 0:
            print('\n---- STORE MENU ----')
            print('1) Find Items By Category')
            print('2) Add Item to Store')
            print('3) Remove Item From Store')
            print('0) Return to Main Menu')
            choice = int(input('> '))

            if choice == 1:
                self.show_items_by_category()
            elif choice == 2:
                self.add_item_to_store()
            elif choice == 3:
                self.remove_item_from_store()
            elif choice != 0:
                print('\nInvalid Choice\n')

    def show_items_by_category(self):
        pass

    def add_item_to_store(self):
        pass

    def remove_item_from_store(self):
        pass