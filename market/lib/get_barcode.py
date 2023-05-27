import secrets
import string
import barcode
from barcode.writer import SVGWriter
from pathlib import Path

path = Path('./market/static/barcodes/')
#path = Path('.')
a = string.ascii_letters + string.digits

barcode_format = barcode.get_barcode_class('code128')

class barcode:
    value = ''.join(secrets.choice(a) for i in range(24))

    def __repr__(self):
        return f'{self.value}'

    def image(self):
        with open(path/'{}.svg'.format(self.value), 'wb') as f:
            barcode_format(self.value, writer=SVGWriter()).write(f)