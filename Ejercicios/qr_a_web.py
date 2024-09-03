import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=7,
                   border=2)

qr.add_data("https://www.hangarxxi.com")
qr.make(fit=True)

img = qr.make_image(fill_colar="black", back_color="white")
img.save('qr_a_web.png')