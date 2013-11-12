#!/usr/bin/env python3

import re
import sys


def help():
    print("Usage:")
    print("categoryConvert.py filename")
    sys.exit(1)

categoryPattern = re.compile('Category\w+')
categories = set()


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        fContents = []
        with open(filename, 'r') as f:
            fContents = f.readlines()
        #penult = fContents[-2]
        lastLine = fContents[-1]
        # Check the last line for a list of categories
        for cat in categoryPattern.findall(lastLine):
            categories.add(cat)
        catStr = 'categories: '
        for cat in categories:
            # Change 'CategoryFoo' to 'foo'
            cat = cat[8:].lower()
            catStr += cat + ' '
        print(catStr)
        # Find the category section and snip it off
        # because we have no rindex()
        rfContents = [x.strip() for x in reversed(fContents)]
        separator = rfContents.index('----')
        if separator != -1:
            fContents = fContents[:len(fContents) - separator - 1]
        with open(filename, 'w') as f:
            f.write("---\n")
            f.write("format: markdown\n")
            f.write(catStr + "\n")
            f.write("...\n")
            for i in fContents:
                f.write(i)

    else:
        help()


if __name__ == '__main__':
    main()
