
import argparse
import finda.finda

if __name__ == "__main__":
    description = "Finds files that have the given string(s) in file name, path or text file contents.  If path(s) are not given all local disks are searched."
    parser  = argparse.ArgumentParser()
    parser.add_argument('-s', '--strings', metavar='string', required=True, nargs='*', help='string(s) to search for - can contain wildcards or regexs')
    parser.add_argument('-p', '--paths', metavar='path', default = ['.'], nargs='*', help="paths to search - can include folders/directories and/or disks and contain wildcards")
    parser.add_argument('-v', '--verbose', action='store_true', help="output status messages during execution")
    args = parser.parse_args()

    finder = finda.finda.Finda(args.strings, args.paths, args.verbose)
    finder.run()
    finder.print()

