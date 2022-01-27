import random
import string


def isValid(password, length):
    flag = False
    password = password[:length]
    if len(password) == length:
        symbols = "!@#$%^&*()_}{[]"
        nums = "0123456789"

        lowercase_letters = [c for c in password if c.islower()]
        uppercase_letters = [c for c in password if c.isupper()]
        symbolsInPassword = [c for c in password if c in symbols]
        numsInPassword = [c for c in password if c in nums]

        if lowercase_letters and uppercase_letters and symbolsInPassword and numsInPassword:
            flag = True

    if flag:
        return True
    return False


def createPassword():
    password = ""
    length = 12

    for _ in range(length):
        randomLowerletters = random.choice(string.ascii_lowercase)
        randomUpperletters = random.choice(string.ascii_uppercase)

        randomInt = random.randint(0,10)
        randomSymbols = random.choice(random.sample("!@#$%^&*()_}{[]",len("!@#$%^&*()_}{[]")))

        options = [randomSymbols,randomLowerletters,randomUpperletters ,str(randomInt)]

        password += random.choice(options)
    return (password,length)

while (True):
    if isValid(createPassword()[0], createPassword()[1]):
        print (createPassword()[0])
        break
    else:
        continue

