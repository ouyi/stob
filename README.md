![Build Status](https://github.com/ouyi/stob/workflows/main/badge.svg)

# stob -- structured text obfuscator

## Overview 

Stob is a tool for obfuscating structured text files, e.g., tsv or csv files.
Those text files are structured such that each line can be splitted into a
constant number of fields using the same delimiter. The tool replaces each
specified field by a random string of the same length as the original field.

## Usage examples

### Input file

    $ cat test.txt
    aa,1,3
    bb,2,2
    bb,ac,1

### Obfuscate the first and the second columns

    $ ./stob.py test.txt -d, -f 0 1
    eW,r,3
    bX,T,2
    s7,R6,1

### The index of the non-nummeric columns can be detected using the included strdet.py script

    $ ./strdet.py -d, test.txt
    0 1 

### The above examples combined

    $ ./stob.py test.txt -d, -f $(./strdet.py -d, test.txt)
    ot,a,3
    tG,0,2
    mR,jW,1
