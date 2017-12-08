import os
import json

#pulls asingle line from a file
def read(filename, line=False):
    try:
        filename = open(filename, "r")
        text = filename.readlines()
        filename.close()
        if not line:
            line = text[line].rstrip()
            return line
        else:
            return text
    except Exception as e:
        print('ERROR fileHandler.py read(filename,line)\n      ',e)

def readjson(filename):
    if True:
        filename = open(filename, "r")
        output = filename.readlines()
        text = ""
        for i in range(0, len(output)):
            text = text + output[i].replace("\n","")
        filename.close()
        return text
    try:
        s = 0
    except Exception as e:
        print('ERROR fileHandler.py readjson(filename,line)\n      ',e)

#writes a single line into a file (don't have to excist)
def write(filename, line, text):
    try:
        t = []
        registratedExistance = False
        while not registratedExistance:
            try:
                f = open(filename, "r")
                t = f.readlines()
                f.close()
                registratedExistance = True
                if t[-1] == '':
                    t.pop(len(t) - 1)
            except Exception:
                f = open(filename, "w")
                f.close()
        if len(t) < line:
            for count in range(len(t), line):
                t.append('\n')
        t[line - 1] = text+'\n'
        try:
            os.remove(filename)
        except Exception:
            something = 0
        f = open(filename, "w")
        for count in range(0, len(t)):
            f.write(t[count])
        f.close()
    except Exception as e:
        print('ERROR fileHandler.py write(filename,line,text)\n      ',e)

def writejson(filename, data):
    #print("data to write by fileHandler.writejson" + str(data))
    with open(filename, "w") as jsonFile:
        json.dump(data, jsonFile, sort_keys=True, indent=2)

#returns the amount of Lines of a file
def getLines(filename):
    try:
        t = []
        f = open(filename, "r")
        t = f.readlines()
        f.close()
        return len(t)
    except Exception as e:
        print('ERROR fileHandler.py getLines(filename)\n      ',e)

#deletes a file
def delete(filename):
    try:
        try:
            os.remove(filename)
        except Exception as e:
            pass
    except Exception as e:
        print('ERROR fileHandler.py delete(filename)\n      ', e)

#creates a file
def create(filename, data=False):
    try:
        if not data:
            f = open(filename, "w")
            f.close()
        elif str(type(data)) == "<class 'list'>":
            with open(filename,'wb') as f:
                f.write(b''.join(data))
        else:
            e = "CustomError: Parameters con only be 'False' or bytelist."
            print('ERROR fileHandler.py create(filename)\n      ', e)
    except Exception as e:
        print('ERROR fileHandler.py create(filename)\n      ',e)