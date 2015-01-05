import ConfigParser
import argparse


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


argp = argparse.ArgumentParser(description='Determin differences between plone version settings')
argp.add_argument('filename1', metavar='FILE1',
                  help='filename of the first config file to read')
argp.add_argument('filename2', metavar='FILE2',
                  help='filename of the second config file to read')
args=argp.parse_args()

conf1 = ConfigParser.ConfigParser()
conf1.read(args.filename1)
versions1 = getDict(conf1)

conf2 = ConfigParser.ConfigParser()
conf2.read(args.filename2)
versions2 = getDict(conf2)

printDiffs(versions1, versions2)
