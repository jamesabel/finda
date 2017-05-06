
import argparse
import finda.finda
import finda.license

if __name__ == "__main__":
    description = "Finds files that have the given string(s) in file name, path or text file contents.  If path(s) are not given all local disks are searched."
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--strings', metavar='string', nargs='*', help='string(s) to search for - can contain wildcards or regexs')
    parser.add_argument('-e', '--exclude', metavar='string', default=[], required=False, nargs='*', help='string(s) to exclude in the search')
    parser.add_argument('-p', '--paths', metavar='path', default=['.'], nargs='*', help="paths to search - can include folders/directories and/or disks and contain wildcards")
    parser.add_argument('-c', '--case', action='store_true', help="take case into account, i.e. case sensitive (default is case insensitive)")
    parser.add_argument('-l', '--license', action='store_true', help="print license info (finda is copyright James Abel)")
    parser.add_argument('-v', '--verbose', action='store_true', help="output status messages during execution")
    args = parser.parse_args()

    if args.license:
        print(finda.license.LICENCE)
    else:
        if args.strings:
            finder = finda.finda.Finda(args.strings, args.exclude, args.paths, args.case, args.verbose)
            finder.run()
            finder.print()
        else:
            print('-s/--strings argument required (use -h/--help for help)')
