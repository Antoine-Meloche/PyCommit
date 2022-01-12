import sys
from .pycommit import *

def main():
    pycommit = PyCommit()
    if len(sys.argv) == 1 or (len(sys.argv) == 3 and sys.argv.contains("-p")):
        pycommit.all()
    elif len(sys.argv) == 2:
        with sys.argv[1] as arg:
            if arg == ("a" or "add"):
                pycommit.add()
            elif arg == ("c" or "commit"):
                pycommit.commit_only()
            elif arg == ("p" or "push"):
                pycommit.push_only()
            else:
                args = arg.split('')
                for arg in args:
                    if arg == "a":
                        pycommit.add()
                    elif arg == "c":
                        pycommit.commit_only()
                    elif arg == "p":
                        pycommit.push_only()
                    else:
                        print(
                            f"{colors.RED}ERROR: Invalid argument: {sys.argv[1]}{colors.RESETC}")
                        sys.exit(1)
    else:
        for arg in sys.argv[1:]:
            if arg == ("a" or "add"):
                pycommit.add()
            elif arg == ("c" or "commit"):
                pycommit.commit_only()
            elif arg == ("p" or "push"):
                pycommit.push_only()
            else:
                try:
                    p_index = sys.argv.index("-p")
                except IndexError:
                    pass

                if arg != ("p" or sys.argv[p_index+1]):
                    print(
                        f"{colors.RED}ERROR: Invalid argument: {arg}{colors.RESETC}")
                    sys.exit(1)

if __name__ == "__main__":
    main()