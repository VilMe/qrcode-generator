import qrcode



class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)