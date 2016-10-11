#! /usr/bin/env python3

try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract

a = pytesseract.image_to_string(Image.open('./getPassCodeNew.jpeg'))
print(a)
