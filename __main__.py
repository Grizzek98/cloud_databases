
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from shopping_cart.main_menu import MainMenu

cred = credentials.Certificate("untracked_files\\ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

def main():
    main_menu = MainMenu()
    main_menu.menu_loop()

if __name__ == '__main__':
    main()