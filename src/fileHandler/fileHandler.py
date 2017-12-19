import json
import os


def read(filePath, line=False):  # pulls a single line from a file
    try:
        readFile = open(filePath, "r")
        lines = readFile.readlines()
        readFile.close()
        if not line:
            line = lines[line].rstrip()
            return line
        else:
            return lines
    except Exception as e:
        print('ERROR fileHandler.py read(filePath,line)\n      ', e)


def readjson(filePath):
    if True:
        jsonFile = open(filePath, "r")
        lines = jsonFile.readlines()
        json = ""
        for i in range(len(lines)):
            json = json + lines[i].replace("\n", "")
        jsonFile.close()
        return json
    try:
        pass
    except Exception as e:
        print('ERROR fileHandler.py readjson(filename,line)\n      ', e)


def write(filePath, line, text):  # writes a single line into a file (doesn't have to exist)
    try:
        lines = []
        registratedExistence = False
        while not registratedExistence:
            try:
                f = open(filePath, "r")
                lines = f.readlines()
                f.close()
                registratedExistence = True
                if lines[-1] == '':
                    t.pop(len(lines) - 1)
            except Exception:
                f = open(filePath, "w")
                f.close()
        if len(lines) < line:
            for count in range(len(t), line):
                lines.append('\n')
        lines[line - 1] = text + '\n'
        try:
            os.remove(filePath)
        except Exception:
            pass
        f = open(filePath, "w")
        for count in range(len(lines)):
            f.write(lines[count])
        f.close()
    except Exception as e:
        print('ERROR fileHandler.py write(filename,line,text)\n      ', e)


def writejson(filePath, data):
    # print("data to write by fileHandler.writejson" + str(data))
    with open(filePath, "w") as jsonFile:
        json.dump(data, jsonFile, sort_keys=True, indent=2)


# returns the amount of lines in a file
def getLines(filePath):
    try:
        t = []
        f = open(filePath, "r")
        t = f.readlines()
        f.close()
        return len(t)
    except Exception as e:
        print('ERROR fileHandler.py getLines(filePath)\n      ', e)


# deletes a file
def delete(filePath):
    try:
        try:
            os.remove(filePath)
        except Exception as e:
            pass
    except Exception as e:
        print('ERROR fileHandler.py delete(filePath)\n      ', e)


# creates a file
def create(filePath, data=False):
    try:
        if not data:
            f = open(filePath, "w")
            f.close()
        elif str(type(data)) == "<class 'list'>":
            with open(filePath, 'wb') as f:
                f.write(b''.join(data))
        else:
            e = "CustomError: Parameters con only be 'False' or bytelist."
            print('ERROR fileHandler.py create(filePath)\n      ', e)
    except Exception as e:
        print('ERROR fileHandler.py create(filePath)\n      ', e)
