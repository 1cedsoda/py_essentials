import hashlib
import os
import platform
import json
from py_essentials import xcptns

# generates any checksum of a file


def fileChecksum(filename, algorithm='sha1', printing=False):
    if algorithm == "sha256":
        hasher = hashlib.sha256()
    elif algorithm == "sha512":
        hasher = hashlib.sha512()
    elif algorithm == "sha1":
        hasher = hashlib.sha1()
    elif algorithm == "md5":
        hasher = hashlib.md5()
    else:
        raise xcptns.UnsupportedHashingalgorithm("fileChecksum()", algorithm, ["md5", "sha1", "sha265", "sha512"])
    try:
        try:
            with open(filename, 'rb') as afile:
                buf = afile.read(65536)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(65536)
            checksum = hasher.hexdigest()
            if printing:
                print(filename + " - " + checksum)
            return checksum
        except PermissionError:
            return "ERROR"
    except Exception as e:
        raise xcptns.StrangeError("fileChecksum()", e)

# generates any checksum of a file


def checksum(data, algorithm='sha1', printing=False):
    if algorithm == "sha256":
        hasher = hashlib.sha256(data.encode())
    elif algorithm == "sha512":
        hasher = hashlib.sha512(data.encode())
    elif algorithm == "sha1":
        hasher = hashlib.sha1(data.encode())
    elif algorithm == "md5":
        hasher = hashlib.md5(data.encode())
    else:
        raise xcptns.UnsupportedHashingalgorithm("fileChecksum()", algorithm, ["md5", "sha1", "sha265", "sha512"])
    checksum = hashlib.hasher.hexdigest()
    if printing:
        print(checksum)
    return checksum
    
# return True if a file excists and False if not
def isFile(object):
    try:
        os.listdir(object)
        return False
    except Exception:
        return True


# creates a treeview of a directory with the filehshes
def createHashtree(directory, algorithm='sha1'):
    if platform.system() == 'Linux':
        slash = '/'
    elif platform.system() == 'Windows':
        slash = '\\'
    directory = directory + slash
    checksum = ''
    jsonstring = '{'
    objects = os.listdir(directory)
    for i in range(0, len(objects)):
        filename = directory + objects[i]
        if isFile(filename):
            checksum = fileChecksum(filename, algorithm)
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
