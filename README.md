# python-essentails

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fb8bedc284324df8bbcb5f1a7d98f3f9)](https://www.codacy.com/app/phyyyl/py-essentails?utm_source=github.com&utm_medium=referral&utm_content=phyyyl/py-essentails&utm_campaign=badger)

A collection of simple python algorythms and functions.
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e00160a21f7c4df8929ca6b0bc5ff5ed)](https://www.codacy.com/app/phyyyl/py-essentails?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=phyyyl/py-essentails&amp;utm_campaign=Badge_Grade)

# File handling (filehandler.py)
required python modules:
    os (standart)
functions:
    singlePull(file, line)             reads a single line from a file
    singlePush(file, line, text)       writes text into any single line of a file
    getLenght(file)                    returns the amount of lines in a file
    delete(file)                       deletes a file
    create(file)                       creates a file
    
# Printing with color (advancedPrint.py)
required python modules:
    sys (standart)
functions:
    effect(effect)                     execute this to set the color effect or reset the color
                                       for the following text prints. (blue, red, bold, reset, ...)
    effectXY(x, y)                     very special custom printing effects. (look into the code)
    clean()                            cleans up the terminal by creating 100 empty lines.
    
