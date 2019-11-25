import argparse
import hashlib
import json
from pathlib import Path
from typing import Union

ALGO_DICT = {
 "sha256": hashlib.sha256(),
 "sha512": hashlib.sha512(),
 "sha1":  hashlib.sha1(),
 "md5": hashlib.md5(),
}

SUPPORTED_ALGOS = list(ALGO_DICT)
CHUNK_SIZE = 64 * 1024


def fileChecksum(
        file_path: Union[str, Path],
        algorithm: str = 'sha1',
        printing: bool = False
):
    """generates any checksum of a file"""
    if type(file_path) is str:
        file_path = Path(file_path)
    if algorithm in SUPPORTED_ALGOS:
        hasher = ALGO_DICT[algorithm]
    else:
        raise ValueError(f'Received: `{algorithm}` but expected one of {", ".join(SUPPORTED_ALGOS)}')
    try:
        with open(file_path, 'rb') as file:
            buf = file.read(CHUNK_SIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(CHUNK_SIZE)
        checksum = hasher.hexdigest()
    except Exception as e:
        checksum = type(e).__name__
    if printing:
        print(f'{file.name} - {checksum}')
    return checksum


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
        raise ValueError(f'Received: `{algorithm}` but expected one of {", ".join(SUPPORTED_ALGOS)}')
    checksum = hashlib.hasher.hexdigest()
    if printing:
        print(checksum)
    return checksum


def createHashtree(
        directory: Union[str, Path],
        algorithm: str = 'sha1'
):
    """creates a tree view of a directory with the file hashes"""
    if type(directory) is str:
        directory = Path(directory)
    objects = [obj for obj in directory.iterdir()]
    hashTree = {
        obj.name:
            fileChecksum(obj, algorithm)
            if obj.is_file()
            else createHashtree(obj, algorithm)
        for obj in objects
    }
    return hashTree


def main(args: argparse.Namespace):
    directory = Path(args.directory)
    if not directory.exists():
        raise FileExistsError(f'{directory} does not seem to exist')
    data = createHashtree(directory, "md5")
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('directory')
    a = p.parse_args()
    main(a)
