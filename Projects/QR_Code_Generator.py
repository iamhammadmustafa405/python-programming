# 04.QR Code Generator.
# 1.Simple

# import qrcode as qr
# img= qr.make("https://www.youtube.com/@HammadMustafapk405")
# img.save("Hammad Mustafa Youtube.png")

# 2. Advance

# import qrcode
# from PIL import Image
# qr= qrcode.QRCode(version=1,error_correction= qrcode.constants.ERROR_CORRECT_H,box_size=10,border= 4)
# qr.add_data("https://www.youtube.com/@HammadMustafapk405")
# qr.make(fit=True)
# img= qr.make_image(fill_color="red",back_color= "blue")
# img.save("Hammad Mustafa Youtube.png")




# 3. Using Input:

import qrcode
from PIL import Image
qr= qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size= 20,border=8)

data= input("Enter URL or txt: ")
qr.add_data(data)
qr.make(fit= True)
fill= input("Enter the fill Color: ")
back= input("Enter the back color: ")
img=qr.make_image(fill_color= fill, back_color= back)
name= input("Enter the name of the file: ")
img.save(name + ".png")