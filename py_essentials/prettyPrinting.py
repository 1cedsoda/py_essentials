import sys


def clean():
    print("\n" * 100)


def effect(effect):
    if effect == "red":
        return sys.stdout.write("\033[1;31m")
    elif effect == "blue":
        return sys.stdout.write("\033[1;34m")
    elif effect == "darkblue":
        return sys.stdout.write("\033[1;94m")
    elif effect == "cyan":
        return sys.stdout.write("\033[1;36m")
    elif effect == "yellow":
        return sys.stdout.write("\033[1;93m")
    elif effect == "purple":
        return sys.stdout.write("\033[1;35m")
    elif effect == "green":
        return sys.stdout.write("\033[1;32m")
    elif effect == "reset":
        return sys.stdout.write("\033[0;0m")
    elif effect == "bold":
        return sys.stdout.write("\033[;1m")
    elif effect == "reverse":
        return sys.stdout.write("\033[;7m")


def effectXY(x, y):
    return sys.stdout.write("\033[" + str(x) + ";" + str(y) + "m")

if __name__ == "__main__":  # see the possibilities of printing
    for y in range(0, 108):
        try:
            sys.stdout.write("\033[" + str(y) + "m")
            print('sys.stdout.write("\\033[' + str(y) + 'm")')
            sys.stdout.write("\033[0;0m")
        except Exception:
            continue
    for x in range(0, 108):
        for y in range(0, 50):
            try:
                sys.stdout.write("\033[" + str(x) + ";" + str(y) + "m")
                print('sys.stdout.write("\\033[' + str(x) + ';' + str(y) + 'm")')
                sys.stdout.write("\033[0;0m")
            except Exception:
                continue
        for y in range(90, 108):
            try:
                sys.stdout.write("\033[" + str(x) + ";" + str(y) + "m")
                print('sys.stdout.write("\\033[' + str(x) + ';' + str(y) + 'm")')
                sys.stdout.write("\033[0;0m")
            except Exception:
                continue
    input()
