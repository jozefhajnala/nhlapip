"""Implementation of the CLI of nhlapip"""
import sys

# Use dynamic import with
# https://docs.python.org/2/library/importlib.html#importlib.import_module
from .player import Player # pylint: disable=unused-import
from .team import Team # pylint: disable=unused-import
from .tournament import Tournament # pylint: disable=unused-import
from .schedule import Schedule # pylint: disable=unused-import
from .standings import Standings # pylint: disable=unused-import
from .md_endpoints import * # pylint: disable=unused-wildcard-import,wildcard-import
from .minor_endpoints import * # pylint: disable=unused-wildcard-import,wildcard-import

def process_args(args):
    """Processes command line arguments"""
    if len(args) == 1:
        print("""
          Usage: nhlapip Endpoint [args]
          Example: nhlapip Player 8451101 8451102
        """)
        return False

    endpoint = args[1]
    # This needs to be endpoint-specific
    # e.g for Tournaments() we need suffixes
    ids = args[2:]
    return (endpoint, ids)

def main():
    """Retrieves data from NHL API based on a CLI command"""
    args = process_args(sys.argv)
    if not args:
        return 0

    # Make this processing better
    constructor = globals()[args[0]]
    if len(args[1]) == 0:
        instance = constructor()
        instance.get_data()
        print(instance.data)
    else:
        instance_list = [constructor(i) for i in args[1]]
        for this_instance in instance_list:
            print(this_instance.get_data())

    return 0

if __name__ == "__main__":
    main()
