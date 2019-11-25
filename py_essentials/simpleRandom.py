# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import random
import string

global HEXCHARS
HEXCHARS = '1234567890abcdef'


def randomString(
        digits,
        chars=string.ascii_uppercase,
        numbers=True,
        uppercase=False
):
    randstring = ''.join(
        random.choice(chars + string.digits)
        for _ in range(digits)
    )
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
    global HEXCHARS
    r = randomString(2, 'abcdef')
    g = randomString(2, 'abcdef')
    b = randomString(2, 'abcdef')
    return "#" + r + g + b


def coinflip():
    return random.choice([True, False])
