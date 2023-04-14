import secrets, string
import code128
from pathlib import Path

path = Path('.')/'market/static/barcodes/'
a = string.ascii_letters + string.digits

class barcode:
    value = ''.join(secrets.choice(a) for i in range(24))

    def image(value):
        with open('{}.svg'.format(value), 'w') as f:
            f.write(code128.svg('{}'.format(value)))