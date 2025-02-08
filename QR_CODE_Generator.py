import qrcode
from PIL import Image
import qrcode.constants

Ranjan=qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_H,
                     box_size=15,
                     border=5)
Ranjan.add_data("https://www.instagram.com/m_ranjan_mohanty_45?igsh=bmZ1bmYwbmtlbjVp")
Ranjan.make(fit=True)
img=Ranjan.make_image(fill_color="green",back_color="black")
img.save("@M_RANJAN_MOHANTY_45.png")