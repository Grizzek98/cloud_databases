import firebase_admin
from firebase_admin import credentials
from shopping_cart.main_menu import MainMenu

# inserting the filapath to your Service Account Key while initializing the firebase
# connection allows the db to check your credentials
cred = credentials.Certificate("untracked_files\\ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

def main():
    main_menu = MainMenu()
    main_menu.menu_loop()

if __name__ == '__main__':
    main()