from __future__ import print_function
import argparse
import os

from isort import isort


def main(argv=None):
    def imports_incorrect(filename):
        return isort.SortImports(filename, check=True).incorrectly_sorted

    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--silent-overwrite', action='store_true', dest='silent')
    parser.add_argument('--force_single_line', action='store_true', dest='force_single_line')
    parser.set_defaults(silent=False, force_single_line=False)
    args = parser.parse_args(argv)

    return_value = 0

    for filename in args.filenames:
        if imports_incorrect(filename) is True:
            if args.silent is False:
                return_value =  1
                isort.SortImports(filename, force_single_line=args.force_single_line)
                print('FIXED: {0}'.format(os.path.abspath(filename)))
            else:
                isort.SortImports(filename, force_single_line=args.force_single_line)
    return return_value

if __name__ == '__main__':
    exit(main())
