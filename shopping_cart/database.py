from firebase_admin import firestore


class Database:

    def __init__(self):
        self.db = firestore.client()



    def view_by_category(self):
        print('\nPlease enter number for desired category (0 to return):')
        # get all collections in top level of db
        col_result = self.db.collections()

        # enumerate through all collections to create menu
        collections = []
        for num, record in enumerate(col_result):
            print(f'{num+1}) {record.id}')
            collections.append(record.id)

        # user chooses a category
        choice = None
        while choice != 0:
            choice = int(input('> '))
            if choice == 0:
                return

            try:
                product_list = self.db.collection(collections[choice-1]).get()
                print()

                # enumerate through documents
                for num, doc in enumerate(product_list):
                    print(f'{num+1}) {(doc.to_dict()).get("name")} - ${(doc.to_dict()).get("price"):.2f}')
                choice = 0
            except:
                print('\nInvalid Choice\n')

    def return_product_list(self):
        print('\nPlease enter number for desired category:')
        # get all collections in top level of db
        col_result = self.db.collections()

        # enumerate through all collections to create menu
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
                product_list = self.db.collection(collections[choice-1]).get()
                choice = 0
                return product_list
            except:
                print('\nInvalid Choice\n')

    def add_item(self):
        pass

    def remove_item(self):
        pass