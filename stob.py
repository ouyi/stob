#!/usr/bin/env python
from lob import *
import fileinput

def main():
    parser = argparse.ArgumentParser(description="""
stob (structured text file obfuscator) obfuscates the input text file, which
has to be structured in that each line can be splitted into a constant number
of fields using the same delimiter. For each line and for each field specified
with the field indicies, the tool replaces the field by a
random string of the same field length.
        """)

    parser.add_argument("-d", "--delimiter", help="delimiter for splitting the line into fields")
    parser.add_argument("-f", "--fields", nargs='+', type=int, help="indicies of the fields to be obfuscated")
    parser.add_argument("-s", "--seed", type=int, help="seed used for the random generator")
    parser.add_argument("filename", help="the input file")
    args = parser.parse_args()

    if args.seed:
        random.seed(args.seed)

    delimiter = None if not args.delimiter else args.delimiter.decode('string_escape')

    for line in fileinput.input(args.filename):
        print convert(line.strip(), delimiter, args.fields)

if __name__ == "__main__":
    main()
