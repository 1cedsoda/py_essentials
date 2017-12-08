import os

#pulls asingle line from a file
def singlePull(file, line):
    file = open(file, "r")
    text = file.readlines()
    file.close()
    line = text[line].rstrip()
    return line

#writes a single line into a file (don't have to excist)
def singlePush(file, line, text):
    t = []
    registratedExistance = False
    while not registratedExistance:
        try:
            f = open(file, "r")
            t = f.readlines()
            f.close()
            registratedExistance = True
            if t[-1] == '':
                t.pop(len(t) - 1)
        except Exception:
            f = open(file, "w")
            f.close()
    if len(t) < line:
        for count in range(len(t), line):
            t.append('\n')
    t[line - 1] = text+'\n'
    try:
        os.remove(file)
    except Exception:
        something = 0
    f = open(file, "w")
    for count in range(0, len(t)):
        f.write(t[count])
    f.close()

#returns the amount of Lines of a file
def getLenght(file):
    t = []
    f = open(file, "r")
    t = f.readlines()
    f.close()
    return len(t)

#deletes a file
def delete(file):
    try:
        os.remove(file)
    except Exception as e:
        something = 0

#creates a file
def create(file):
    f = open(file, "w")
    f.close()