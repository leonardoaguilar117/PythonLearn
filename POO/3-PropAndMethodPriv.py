import secrets
import qrcode


class RandGeneratorQR:
    # Private attributes and methods are a safe way to use them,
    # as they can only be modified within this class and not in others.
    def __init__(self, URL, Directory, Size):
        self.__URL = URL
        self.__Directory = Directory
        self.__box_size = Size

        qr = qrcode.QRCode(
            version=4,
            box_size=Size,
            border=3
        )

    def getUrl(self):
        return self.__URL

    def createQR(self):
        img = qrcode.make(self.__URL)
        img.save(self.__Directory)
        img.show()

    @classmethod
    def default(cls):
        return RandGeneratorQR("www.google.com", "C:/Users/leona/Downloads/Python/image.png", 10)


if __name__ == "__main__":
    QR = RandGeneratorQR(
        "www.youtube.com", "C:/Users/leona/Downloads/Python/image.png", 10)
    QR.createQR()
