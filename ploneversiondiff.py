#!/usr/bin/env python2

import ConfigParser
import argparse
import distutils.version

show_all = False

def getDict(config):
    """extract versions from a config into a dictionary"""
    opts = config.options('versions')
    d={}
    for x in opts:
        d[x] = config.get('versions',x)
    return d


def printDiffs(d1, d2, only_newer=False):
    """print differing items of dictionaries to stdout"""
    for key in d1:
        if key in d2:
            vstring1 = d1[key]
            v1 = distutils.version.LooseVersion(vstring1)
            vstring2 = d2[key]
            v2 = distutils.version.LooseVersion(vstring2)
            # print the version difference, don't print the version
            # difference if only_newer is activated and the version of
            # the second dict is smaller (older) then the version of
            # the first dict
            if ((v1 != v2) and ((not only_newer) or (v1 < v2))):
                print("%s\n\t%s\t%s" % (key, vstring1, vstring2))

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


argp = argparse.ArgumentParser(\
    description='Determin differences between plone version settings')
argp.add_argument('filename1', metavar='FILE1',
                  help='filename of the first config file to read')
argp.add_argument('filename2', metavar='FILE2',
                  help='filename of the second config file to read')
argp.add_argument('-a', '--show-all',default=False, action='store_true',
                  help='When passed, the program will show all differences, '
                       'not only those of versions set in both files.')
argp.add_argument('-n', '--only-newer', default=False, action='store_true',
                  help='When passed, the program will only show differences '
                  'when the version of FILE2 is higher than the version of '
                  'FILE1')

args=argp.parse_args()

conf1 = ConfigParser.ConfigParser()
conf1.read(args.filename1)
versions1 = getDict(conf1)

conf2 = ConfigParser.ConfigParser()
conf2.read(args.filename2)
versions2 = getDict(conf2)

printDiffs(versions1, versions2, only_newer=args.only_newer)

if args.show_all:
    print("")
    printNotMatching((versions1, args.filename1), (versions2, args.filename2))
