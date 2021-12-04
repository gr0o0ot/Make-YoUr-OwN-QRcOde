import qrcode
import image

qr = qrcode.QRCode(
    version= 15,
    box_size=10,
    border = 5

)
data = "https://github.com/gr0o0ot"  # by scanning  the qr code it will take to my github profile.

qr.add_data(data)
qr.make(fit=True)

image  = qr.make_image(fill = "black", back_color = "white")
image.save("mihir_qr1.png")