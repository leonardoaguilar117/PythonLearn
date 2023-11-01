import secrets
import string

# rand is not a secure library, because the "random" generator, is bassed in a
# predictible secuence, wheiter, secrets is better


def randomKeyGenerator(length):
    randString = string.ascii_letters + string.digits
    Key = ""

    while length != 0:
        Key += secrets.choice(randString)
        length -= 1
    return Key


if __name__ == "__main__":
    print(randomKeyGenerator(8))
