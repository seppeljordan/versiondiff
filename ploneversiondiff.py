#!/usr/bin/env python2

import ConfigParser
import argparse

show_all = False

def getDict(config):
    """extract versions from a config into a dictionary"""
    opts = config.options('versions')
    d={}
    for x in opts:
        d[x] = config.get('versions',x)
    return d


def printDiffs(d1, d2):
    """print differing items of dictionaries to stdout"""
    for key in d1:
        if key in d2:
            if d1[key] != d2[key]:
                print("%s\n\t%s\t%s" % (key, d1[key], d2[key]))

def printNotMatching((d1,filename1), (d2,filename2)):
    """print versions set in only one of the files"""
    print("Versions set in %s, but not set in %s" % (filename1,filename2))
    for key in d1:
        if not (key in d2):
            print("%s: %s" % (key, d1[key]))
    print("")
    print("Versions set in %s, but not set in %s" % (filename2,filename1))
    for key in d2:
        if not (key in d1):
            print("%s: %s" % (key, d2[key]))


argp = argparse.ArgumentParser(description='Determin differences between plone version settings')
argp.add_argument('filename1', metavar='FILE1',
                  help='filename of the first config file to read')
argp.add_argument('filename2', metavar='FILE2',
                  help='filename of the second config file to read')
argp.add_argument('-a', '--show-all',default=False, action='store_true',
                  help='When passed, the program will show all differences, '
                       'not only those of versions set in both files.')
args=argp.parse_args()

conf1 = ConfigParser.ConfigParser()
conf1.read(args.filename1)
versions1 = getDict(conf1)

conf2 = ConfigParser.ConfigParser()
conf2.read(args.filename2)
versions2 = getDict(conf2)

printDiffs(versions1, versions2)

if args.show_all:
    print("")
    printNotMatching((versions1, args.filename1), (versions2, args.filename2))
