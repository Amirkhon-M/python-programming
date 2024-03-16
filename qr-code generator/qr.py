import qrcode
import time

qr = qrcode.QRCode(version=1, box_size=10, border=5)

data = input(": ")


qr.add_data(data)
qr.make(fit=True)

timestamp = int(time.time())
filename = f"qrcode_{timestamp}.png"
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)
print(f"QR code generated for the entered URL. Saved as {filename}")
