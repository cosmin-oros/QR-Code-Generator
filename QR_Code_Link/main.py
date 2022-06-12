import pyqrcode

data = "https://github.com/cosmin-oros"
image = pyqrcode.create(data)
image.svg("QR.svg", scale="5")
print(data)