import sys
from .player import Player
from .team import Team
from .tournament import Tournament
from .schedule import Schedule
from .standings import Standings
from .md_endpoints import *
from .minor_endpoints import *

def processArgs(args):
    print(args)
    if (len(args) == 1):
        print("""
          Usage: nhlapip Endpoint [args]
          Example: nhlapip Player 8451101 8451102
        """)
        return False
    else:
        endpoint = args[1]
        # TODO: This needs to be endpoint-specific
        # e.g for Tournaments() we need suffixes
        ids = args[2:]
        return (endpoint, ids)

def main():
    args = processArgs(sys.argv)
    if args == False:
        return True

    # TODO: Obviously make this processing better
    constructor = globals()[args[0]]
    if len(args[1]) == 0:
        instance = constructor()
        instance.get_data()
        print(instance.data)
    else:
        instancelist = [constructor(i) for i in args[1]]
        [print(x.get_data()) for x in instancelist]

    return True

if __name__ == "__main__":
    main()
