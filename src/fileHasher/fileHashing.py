import hashlib
import os
import platform
import json


# generates common checksums of a file
def genFileChecksum(filePath, algorithm='sha1', printing=False):
    if algorithm.lower() == "sha256":
        hasher = hashlib.sha256()
    elif algorithm.lower() == "sha512":
        hasher = hashlib.sha512()
    elif algorithm.lower() == "sha1":
        hasher = hashlib.sha1()
    elif algorithm.lower() == "md5":
        hasher = hashlib.md5()
    else:
        e = "CustomError: Algorithm", algorithm, 'is not supported. Sha1 will be used. Supported algorithms are "sha1", "sha256" and "sha512".'
        print('ERROR fileHandler.py genFileChecksum(filePath,algorithm)\n      ', e)
        hasher = hashlib.sha1()
    try:
        try:
            with open(filePath, 'rb') as afile:
                buf = afile.read(65536)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(65536)
            checksum = hasher.hexdigest()
            if printing:
                print(filePath + " - " + checksum)
            return checksum
        except PermissionError:
            return "ERROR"
    except Exception as e:
        print('ERROR fileHandler.py genFileChecksum(filePath,algorithm)\n      ', e)
        # print(filePath + " - ERROR")
        return "ERROR"


# return True if a file exists and False if not
def isFile(object):
    return os.path.isfile(object)


# creates a treeview of a directory with the filehashes
def createHashtree(directory, algorithm='sha1'):
    if platform.system() == 'Linux':
        slash = '/'
    elif platform.system() == 'Windows':
        slash = '\\'
    directory = directory + slash
    checksum = ''
    jsonstring = '{'
    objects = os.listdir(directory)
    for i in range(len(objects)):
        filename = directory + objects[i]
        if isFile(filename):
            checksum = genFileChecksum(filename, algorithm)
            jsonstring = jsonstring + '"' + objects[i] + '":"' + str(checksum) + '",'
        else:
            if platform.system() == 'Linux':
                slash = '/'
            elif platform.system() == 'Windows':
                slash = '\\'
            jsonstring = jsonstring + '"' + objects[i] + '":' + createHashtree(directory + objects[i] + slash, algorithm) + ','
    if jsonstring[-1] == "{":
        jsonstring = jsonstring + "}"
    else:
        jsonstring = jsonstring[:-1] + "}"
    return jsonstring

if __name__ == "__main__":
    directory = os.path.dirname(os.path.realpath(__file__))  # working directory
    data = createHashtree(directory, "md5")
    data = json.loads(data)
    print(json.dumps(data, sort_keys=True, indent=4))
