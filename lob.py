#!/usr/bin/env python
import argparse, logging, sys, random, string

def randstr(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in xrange(length))

def obfuscate(fields, indexes = None):
    result = []
    if not indexes:
        result.extend([randstr(len(f)) for f in fields])
    else:
        result.extend(fields)
        for i in indexes:
            result[i] = randstr(len(fields[i]))
    return result

def convert(line, delimiter, indexes):
    fields = [line] if not delimiter else line.split(delimiter)
    obfuscated = obfuscate(fields, indexes)
    return ('' if not delimiter else delimiter).join(obfuscated)

def main():
    parser = argparse.ArgumentParser(description="""lob = lineobfuscator
    replaces each field of the input line by a random string of the same length as the original field.
        """)
    parser.add_argument("-d", "--delimiter", help="delimiter for splitting the line into fields")
    parser.add_argument("-f", "--fields", nargs='+', type=int, help="indexes of the fields to be obfuscated")
    parser.add_argument("-s", "--seed", type=int, help="seed used for the random generator")
    args = parser.parse_args()

    if args.seed:
        random.seed(args.seed)
    delimiter = None if not args.delimiter else args.delimiter.decode('string_escape')
    line = sys.stdin.readline()
    print convert(line.strip(), delimiter, args.fields)

if __name__ == "__main__":
    main()
