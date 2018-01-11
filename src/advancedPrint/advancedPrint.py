import sys

class effects:
    RED = "red"
    BLUE = "blue"
    DARKBLUE = "darkblue"
    CYAN = "cyan"
    YELLOW = "yellow"
    PURPLE = "purple"
    GREEN = "green"
    RESET = "reset"
    BOLD = "bold"
    REVERSE = "reverse"


def clearConsole():
    print("\n" * 100)


def effect(effect):
    if effect == "red":
        return sys.stdout.write("\033[1;31m")
    if effect == "blue":
        return sys.stdout.write("\033[1;34m")
    if effect == "darkblue":
        return sys.stdout.write("\033[1;94m")
    if effect == "cyan":
        return sys.stdout.write("\033[1;36m")
    if effect == "yellow":
        return sys.stdout.write("\033[1;93m")
    if effect == "purple":
        return sys.stdout.write("\033[1;35m")
    if effect == "green":
        return sys.stdout.write("\033[1;32m")
    if effect == "reset":
        return sys.stdout.write("\033[0;0m")
    if effect == "bold":
        return sys.stdout.write("\033[;1m")
    if effect == "reverse":
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
