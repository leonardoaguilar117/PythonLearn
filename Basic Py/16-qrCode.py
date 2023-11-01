# Qr Code is a two dimensional pictographic code used for
# it´s fast readability on a while background
import qrcode


def generateQR(directory, URL):

    qr = qrcode.QRCode(
        version=4,  # is an integer from 1 to 40 that controls the size of the QR Code (
        box_size=10,  # controls the resolution an effectiveness of qr
        border=3,  # add white space around at qr
    )

    # create a qr with the URL assigned
    img = qrcode.make(URL)

    # save the qr in the given directory
    img.save(directory)

    # executes the image
    img.show()


if __name__ == "__main__":
    generateQR("C:/Users/leona/Downloads/Python/image.png",
               "No mames, como me gustas y te haces la dificil :/")
