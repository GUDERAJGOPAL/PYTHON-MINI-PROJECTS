import pyqrcode
import png
from pyqrcode import QRCode
s="Raj gopal"
url=pyqrcode.create(s)
url.png("Raj.png",scale=13)


