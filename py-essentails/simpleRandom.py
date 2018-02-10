# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import random
import string

global hexchars
hexchars = "1234567890abcdef"


def randomString(digits, chars=string.ascii_uppercase, numbers=True, uppercase=False):
    if not numbers:
        numbers = ""
    else:
        numbers = string.digits

    randstring = ''.join(random.choice(chars + string.digits) for _ in range(digits))
    if uppercase:
        return randstring
    else:
        return randstring.lower()


def randomRGB():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, b, g)


def randomHexColor():
    global hexchars
    r = randomString(2, "abcdef")
    g = randomString(2, "abcdef")
    b = randomString(2, "abcdef")
    return "#" + r + g + b


def coinflip():
    x = random.randint(0, 1)
    if x == 1:
        return True
    else:
        return False
