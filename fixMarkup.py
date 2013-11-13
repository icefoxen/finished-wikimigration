#!/usr/bin/env python3
# Grovels through a file and replaces **foo** with *foo*, and vice versa.
# Painfully non-idempotent (though it should be its own inverse).
# Also bulleted lists make life hard.

import re
import sys


def usage():
    print("Usage:")
    print("fixMarkup.py filename")
    sys.exit(1)

def firstNonWhitespaceIndex(s):
    return len(s) - len(s.lstrip())
    
paracount = 0
def convertPara(para):
    global paracount
    paracount += 1
    #print("Converting paragraph {}".format(paracount))
    if para == '':
        return ''
    elif para[:2] == '* ':
        # The para is a bulleted list; handle it specially.
        # We have to be careful to not munge nested lists.
        def pythonNeedsBetterLambdas(x):
            return x[:2] + convertPara(x[2:])
        lineses = para.split('\n')
        fixedlineses = map(pythonNeedsBetterLambdas, lineses)
        return '\n'.join(fixedlineses)
    elif para[0] == ' ':
        # Para is indented and might be a bulleted list.
        # So we strip off the leading whitespace, recurse, and
        # add the whitespace back.  Whew.
        def pythonNeedsBetterLambdas(x):
            start = firstNonWhitespaceIndex(para)
            return (' ' * start) + convertPara(x[start:])
        lineses = para.split('\n')
        fixedlineses = map(pythonNeedsBetterLambdas, lineses)
        return '\n'.join(fixedlineses)
    else:
        accm = ''
        i = 0
        while i < len(para):
            #print("Character {}".format(i))
            if para[i] == '*':
                if (i+1) < len(para) and para[i + 1] == '*':
                    accm += '*'
                    # Skip ahead one extra
                    i += 1
                else:
                    accm += '**'
            else:
                accm += para[i]
            i += 1
        return accm

def parseParas(s):
    """Takes a string and separates it into paragraphs separated by blank lines."""
    paras = s.split('\n\n')
    # Remove empty strings caused by consecutive \n\n's.
    # bool('') == False
    return filter(bool, paras)

def mightAsWellFixHeadingsWhileWeAreAtIt(s):
    # Brute force FTW
    s1 = s.replace('#\n#\n#\n#', '####')
    s2 = s1.replace('#\n#\n#', '###')
    s3 = s2.replace('#\n#', '##')
    return s3

def main():
    if len(sys.argv) <= 1:
        usage()
    fContents = ""
    with open(sys.argv[1], 'r') as f:
        fContents = f.read()
    print("Fixing {}".format(sys.argv[1]))
    fContents = mightAsWellFixHeadingsWhileWeAreAtIt(fContents)
    paras = parseParas(fContents)
    fixedparas = map(convertPara, paras)
    with open(sys.argv[1], 'w') as f:
        for i in fixedparas:
            f.write(i + '\n\n')
            


if __name__ == '__main__':
    main()
