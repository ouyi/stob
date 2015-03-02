#!/usr/bin/env python
import argparse, re, sys
import fileinput

def detect(fields):
    result = [None] * len(fields)
    for i, f in enumerate(fields):
        result[i] = False if re.match(r"""^(-)?[0-9]+(\.[0-9]+)?|.$""", f) else True
    return result

def detectMerge(fields, flags):
    if len(flags) != len(fields):
        raise ValueError("illegal arguments: {} != {}".format(fields, flags))

    result = detect(fields) 
    for i, f in enumerate(flags):
        result[i] = f or result[i]
    return result

def main():
    parser = argparse.ArgumentParser(description="""
strdet (string detector) detects for the input structured text file the indexes of the fields which are non-digital.
        """)

    parser.add_argument("-d", "--delimiter", default="\t", help="delimiter for splitting the line into fields")
    parser.add_argument("filename", help="the input file")
    args = parser.parse_args()

    delimiter = None if not args.delimiter else args.delimiter.decode('string_escape')

    flags = None
    for line in fileinput.input(args.filename):
        fields = line.rstrip().split(delimiter)
        try:
            flags = detect(fields) if not flags else detectMerge(fields, flags)
        except ValueError:
            print >> sys.stderr, fields
            print >> sys.stderr, flags

    for i, flag in enumerate(flags):
        if flag:
            print i,

if __name__ == "__main__":
    main()
