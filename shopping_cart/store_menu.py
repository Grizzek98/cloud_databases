from firebase_admin import firestore

class StoreMenu:

    def __init__(self):
        self.db = firestore.client()

    def menu_loop(self):
        choice = None
        while choice != 0:
            print('\n---- STORE MENU ----')
            print('1) Find Items By Category')
            print('2) Modify Item')
            print('0) Return to Main Menu')
            choice = int(input('> '))

            if choice == 1:
                self.show_items_by_category()
            elif choice == 2:
                self.check_category()
            elif choice != 0:
                print('\nInvalid Choice\n')

    def show_items_by_category(self):
        print('\nPlease enter number for desired category (0 to return):')
        # get all collections in top level of db
        col_result = self.db.collections()
        # collections = self.print_collection_list(col_result)
        collections = []
        for num, record in enumerate(col_result):
            print(f'{num+1}) {record.id}')
            collections.append(record.id)

        choice = None
        while choice != 0:
            choice = int(input('> '))

            try:
                doc_result = self.db.collection(collections[choice-1]).get()
                print()
                for num, doc in enumerate(doc_result):
                    print(f'{num+1}) {(doc.to_dict()).get("name")} - ${(doc.to_dict()).get("price"):.2f}')
                choice = 0
            except:
                print('\nInvalid Choice\n')

    def check_category(self):
        # ask for category
        print('\nPlease enter category number:')
        col_result = self.db.collections()
        collections = []
        choice = None
        while choice != 0:
            print('0) Return')
            print('1) Create New Category')
            indices = []
            for num, record in enumerate(col_result, start=2):
                print(f'{num}) {record.id}')
                indices.append(num)
            choice = int(input('> '))
            if choice in indices:
                self.check_name()
            else:
                # if not, ask if should be added
                while choice != 'n':
                    print('Category does not exist in database. Add it? (y/n)')
                    choice = input('> ')
                    if choice == 'y':
                        self.check_name()
                choice = 0
        
        # ask for name, check if exists
        #   if not, ask if should be added
        #   if yes, ask if item should be removed or modified (price change)
        #       remove : remove item
        #       modified: ask for price
        #           remove item

    def check_name(self):
        choice = None
        while choice != 0:
            try:
                print('Please enter name of product:')

            except:
                pass