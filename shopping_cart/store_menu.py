from shopping_cart.database import Database

class StoreMenu:

    def __init__(self):
        # initialize database object
        self.db = Database()


    def menu_loop(self):
        choice = None
        # print menu options
        while choice != 0:
            print('\n---- STORE MENU ----')
            print('0) Return to Main Menu')
            print('1) Find Items By Category')
            print('2) Add Item to Store')
            print('3) Remove Item from store')
            print('4) Update Item Price')
            choice = int(input('> '))

            if choice == 1:
                self.db.view_by_category()
            elif choice == 2:
                self.add_item_to_store()
            elif choice == 3:
                self.remove_item()
            elif choice == 4:
                self.modify_item()
            elif choice != 0:
                print('\nInvalid Choice - Choose available index')


    def add_item_to_store(self):
        """ adds an item to database with the help of database
            class
        """
        try:
            # get category from database class
            cat = self.db.return_category_add_item()
            # if user exits menu
            if cat == False:
                return
            # if user chooses to create new cat
            if cat == True:
                print('Please enter name of new category:')
                cat = input('> ')
            print('Please enter name of item:')
            name = input('> ')
            print('Please enter price of item:')
            price = float(input('> '))
            # send info to database to add item to db
            self.db.add_item(cat.title(), name.title(), price)
        except:
            print('\nError')

        
    def remove_item(self):
        """ removes an item from the database with the help of
            database class
        """
        # get category from database class
        cat = self.db.return_category_remove_item()
        # if user exits menu
        if cat == False:
            return
        print('Please enter name of product: ')
        name = input('> ')
        # send info to database to remove item
        self.db.remove_item(cat.title(), name.title())


    def modify_item(self):
        """ allows the user to modify an existing product on the 
            database
        """
        # get category from database class
        cat = self.db.return_category_modify_item()
        # if user exits menu
        if cat == False:
            return
        print('Please name of existing product: ')
        name = input('> ')
        print('Please enter new item price:')
        price = float(input('> '))
        # send info to database to modify item
        self.db.modify_item(cat.title(), name.title(), price)