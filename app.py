import argparse
from rectangle import Rectangle

COMMAND_GET_AREA = "get-area"

def main():
    # create a parser object
    parser = argparse.ArgumentParser(description = "A Rectangle Program")
    parser.add_argument('--width', type=float, required=True,
        help='''Width in centimers.''')
    parser.add_argument('--height', type=float, required=True,
        help='''Height in centimers.''')
    subparsers = parser.add_subparsers(dest="subcommand")

     # Create the parser for the "command_1" command.
    subparsers.add_parser(COMMAND_GET_AREA,
                          help='''Calculates and prints the area.''')

    args = parser.parse_args()

    if args.subcommand == COMMAND_GET_AREA:
        r = Rectangle(args.width, args.height)
        print(r.get_area(), flush=True)
    else:
        print("Missing subcommand.")
        

if __name__ == "__main__":
    main()