from firebase_admin import firestore


class Database:

    def __init__(self):
        # initialize firestore client object
        self.db = firestore.client()


    def view_by_category(self):
        print('\nPlease enter number for desired category:')
        # get all collections in top level of db
        col_result = self.db.collections()
        # print category selection menu
        collections = []
        print('0) Return')
        for num, record in enumerate(col_result):
            print(f'{num+1}) {record.id}')
            collections.append(record.id)
        choice = None
        while choice != 0:
            choice = int(input('> '))
            # if user exits menu
            if choice == 0:
                return
            try:
                # get product list from db
                product_list = self.db.collection(collections[choice-1]).get()
                print()
                # print products
                for num, doc in enumerate(product_list):
                    print(f'{num+1}) {(doc.to_dict()).get("name")} - ${(doc.to_dict()).get("price"):.2f}')
                choice = 0
            except:
                print('\nInvalid Choice')


    def return_category_add_item(self):
        """ connect to db to add item to db based on category name, 
            product name, and price - also adds new categories 
        """
        print('\nPlease enter number for desired category:')
        # get all collections in top level of db
        col_result = self.db.collections()
        # print category selection menu
        collections = []
        print('0) Return')
        print('1) Create New Cat')
        choice = None
        while choice != 0:
            for num, record in enumerate(col_result):
                print(f'{num+2}) {record.id}')
                collections.append(record.id)
            try:
                choice = int(input('> '))
                if choice == 0:
                    return False
                if choice == 1:
                    return True
                if choice != 0:
                    return collections[choice-2]
            except ValueError:
                print('Invalid Choice')
            except:
                print('Error')


    def return_category_remove_item(self):
        """ connects to database to remove items based on category name,
            and product name
        """
        print('\nPlease enter number for desired category:')
        # get all collections in top level of db
        col_result = self.db.collections()
        # print category selection menu
        collections = []
        print('0) Return')
        choice = None
        while choice != 0:
            for num, record in enumerate(col_result):
                print(f'{num+1}) {record.id}')
                collections.append(record.id)
            try:
                choice = int(input('> '))
                if choice == 0:
                    return False
                if choice != 0:
                    return collections[choice-1]
            except ValueError:
                print('Invalid Choice')
            except:
                print('Error')


    def return_category_modify_item(self):
        """ connects to database to modify existing items based on
            cat, name, and price
        """
        print('\nPlease enter number for desired category:')
        # get all collections in top level of db
        col_result = self.db.collections()
        # print category selection menu
        collections = []
        print('0) Return')
        choice = None
        while choice != 0:
            for num, record in enumerate(col_result):
                print(f'{num+1}) {record.id}')
                collections.append(record.id)
            try:
                choice = int(input('> '))
                if choice == 0:
                    return False
                if choice != 0:
                    return collections[choice-1]
            except ValueError:
                print('Invalid Choice')
            except:
                print('Error')


    def return_product_list(self):
        print('\nPlease enter number for desired category:')
        # get all collections in top level of db
        col_result = self.db.collections()
        # print category selection menu
        collections = []
        print('0) Return')
        for num, record in enumerate(col_result):
            print(f'{num+1}) {record.id}')
            collections.append(record.id)
        # user chooses a category
        choice = None
        while choice != 0:
            choice = int(input('> '))
            try:
                # get product list from db
                product_list = self.db.collection(collections[choice-1]).get()
                choice = 0
                return product_list
            except:
                print('\nInvalid Choice\n')


    def add_item(self, cat, name, price):
        """ connect to db to add item based on cat, name, and price
        """
        product = {'name': name, 'price': price}
        # add item to db
        self.db.collection(cat).add(product)

  
    def remove_item(self, cat, name):
        """ connect to db to remove item based on cat and name
        """
        # get all documents with name field matching name
        docs = self.db.collection(cat).where('name', '==', name).get()
        for doc in docs:
            key = doc.id
            # remove product from db
            self.db.collection(cat).document(key).delete()
            print(f'\nRemoved "{name}" successfully')

    def modify_item(self, cat, name, price):
        """ connect to db to modify an item's price based on
            cat, name, and price
        """
        # get all documents in cat
        docs = self.db.collection(cat).get()
        for doc in docs:
            if doc.to_dict()['name'] == name:
                key = doc.id
                # modify product price on db
                self.db.collection(cat).document(key).update({'price': price})
                print(f'\nUpdated price of {name} successfully')