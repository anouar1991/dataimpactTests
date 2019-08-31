import json
import csv

AVAILABLE_PRODUCTS_CSV_FILE = 'available_products.csv'
PRODUCTS_BUNDLES_KEY = 'Bundles'
PRODUCTS_KEY = 'Products'


class Product:

    def __init__(self, product, csv_file=None):
        self.message = '[X] No clues about the product availability'
        if 'IsAvailable' in {*product}:
            self.name = product['Name'][0:30]
            self.isAvailable = product['IsAvailable']
            if self.isAvailable:
                self.price = round(product['Price'], ndigits=1)
                self.message = 'You can buy %s at our store at %.1f' % (self.name, self.price)
                self.save_to_csv(csv_file)
            else:
                self.id = product['Stockcode']
                self.message = 'Product id: %s, Product Name: %s' % (self.id, self.name)
        print(self.message)

    def unpack_product_dicts(prod):
        product = {}
        for dct in prod:
            product = {**product, **dct}
        return product

    def save_to_csv(self, csv_file):
        filewriter = csv.writer(csv_file, delimiter=',')
        filewriter.writerow([self.name, self.price])

def main(data_json_path):

    with open(data_json_path, 'r') as datafile, open(AVAILABLE_PRODUCTS_CSV_FILE, 'a+') as csv_file:
        data = json.load(datafile)
        for i, bundle in enumerate(data[PRODUCTS_BUNDLES_KEY]):
            if 'Products' in {*bundle}:
                product = bundle[PRODUCTS_KEY]
                if len(product):
                    Product(Product.unpack_product_dicts(product), csv_file)
                else:
                    print('[X] No clues about the product')
            else:
                print('no product in bundle: %d' % i)


'Products'