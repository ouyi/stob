#!/usr/bin/env python
from lob import *

def main():
    parser = argparse.ArgumentParser(description="""
stob (structured text file obfuscator) obfuscates the input text file, which
has to be structured in that each line can be splitted into a constant number
of fields using the same delimiter. The tool replaces each specified field by a
random string of the same length as the original field.
        """)

    parser.add_argument("-d", "--delimiter", help="delimiter for splitting the line into fields")
    parser.add_argument("-f", "--fields", nargs='+', type=int, help="indexes of the fields to be obfuscated")
    parser.add_argument("-s", "--seed", type=int, help="seed used for the random generator")
    parser.add_argument("inputfile", help="the input file")
    args = parser.parse_args()

    if args.seed:
        random.seed(args.seed)

    delimiter = None if not args.delimiter else args.delimiter.decode('string_escape')

    with open(args.inputfile) as inputfile:
        for line in inputfile:
            print convert(line.rstrip(), delimiter, args.fields)

if __name__ == "__main__":
    main()
