#!/usr/bin/env python3

import argparse

def main(args):
    pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Description of this script.')
    parser.add_argument('arg1', help='A positional argument.')
    parser.add_argument('-a', '--arg2', nargs='?', type=str, metavar='ARG2',help='An optional argument.')
    parser.add_argument('-b', '--arg3', nargs='+', metavar='ARG3', help='Optional one or more argument(s).')
    parser.add_argument('--verbose', action='store_true', default=False, help='Verbose mode when this flag is set.')
    parser.add_argument('--debug', action='store_true', default=False, help='Debug mode when this flag is set.')
    args = vars(parser.parse_args())    # Convert the Namespace object to a dictionary.

    main(args)
